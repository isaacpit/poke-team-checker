import sys
import pprint as pp
from typing import Type

import requests
import json

import time

import logging 

from logging_setup import *

# print = logging.info

SLEEP_BETWEEN_CALLS = True
SLEEP_TIME_PER_CALL = 0.50


class PokeApiGenerator:
  POKE_API_BASE_URL = "https://pokeapi.co/api/v2/"
  GET_ALL_POKEMON_URL = POKE_API_BASE_URL + "pokemon"
  KEY_URL = 'url'

  def get_pokemon_w_limit_query_url(limit: int) -> str:
    logging.debug("Getting pokemon with limit: {}".format(limit))
    return PokeApiGenerator.GET_ALL_POKEMON_URL + "?limit=" + str(limit)

  def loopThroughList(pokeResultsList):
    pokemonInfoResults = [None] * len(pokeResultsList)
    n_pokemon = len(pokeResultsList)
    for i in range(n_pokemon):
      getPokeListResult = pokeResultsList[i]
      PokeApiGenerator.validateGetPokemonApiResponse(getPokeListResult)

      # sleet thread so we don't spam server too quickly

      if SLEEP_BETWEEN_CALLS:
        time.sleep(SLEEP_TIME_PER_CALL)

      a_pokemon_url = getPokeListResult['url']
      logging.info("(%4d/%4s) %s", i+1, n_pokemon, getPokeListResult['name'])
      logging.info("\t%s", a_pokemon_url)
      response = requests.get(a_pokemon_url)
      logging.debug("GetPokemonAPI Reponse Keys\n{}".format(pp.pformat(list(response.json().keys()))))
      extractedObj = PokemonInfoResponse(response.json())
      pokeResultsList[i] = extractedObj.d_data
    
    return pokeResultsList

  def validateGetPokemonApiResponse(getPokeListResult):
    
    if not isinstance(getPokeListResult, dict):
      raise TypeError("getPokemonInfo response invalid")

    if not PokeApiGenerator.KEY_URL in getPokeListResult:
      raise KeyError("getPokemonInfo does not contain key {}".format(PokeApiGenerator.KEY_URL))

class PokemonInfoResponse:
  FIELD_NAME = "name"
  FIELD_SPRITES = "sprites"
  FIELD_STATS = "stats"
  FIELD_TYPES = "types"
  FIELD_ORDER = "order"
  FIELD_FORMS = "forms"
  FIELD_SPECIES = "species"
  DESIRED_FIELDS = [FIELD_NAME, FIELD_SPRITES, FIELD_STATS, FIELD_TYPES, FIELD_ORDER, FIELD_FORMS, FIELD_SPECIES]

  def __init__(self, response_obj):
    self.d_data = {} 
    SHOULD_SNEAK_PEAK_POKE_FIELDS = True

    if SHOULD_SNEAK_PEAK_POKE_FIELDS:
      logging.debug("Sneak Peak of poke fields")
    for k, v in response_obj.items():
      
      if SHOULD_SNEAK_PEAK_POKE_FIELDS:
        logging.debug("{:30} {:20} {}".format(k, str(v)[0:20], k in PokemonInfoResponse.DESIRED_FIELDS))

      if k in PokemonInfoResponse.DESIRED_FIELDS:
        self.d_data[k] = PokemonInfoResponse.transform_data(k, v)

    logging.debug("Final Transformed Data\n%s", json.dumps(self.d_data, indent=2))
    # logging.info(self.d_data.keys())
    
  
  def transform_data(key, value_obj):
    """Takes Pokemon API Response Object and converts to usable form"""  
    if key == PokemonInfoResponse.FIELD_SPRITES:
      return PokemonInfoResponse.helper_transform_sprites(value_obj)
    elif key == PokemonInfoResponse.FIELD_STATS:
      return PokemonInfoResponse.helper_transform_stats(value_obj)
    elif key == PokemonInfoResponse.FIELD_TYPES:
      return PokemonInfoResponse.helper_transform_types(value_obj)
    return value_obj

  def helper_transform_sprites(value_obj):
    return value_obj['front_default']
  def helper_transform_stats(value_obj):
    logging.debug("Stats before transform\n%s", json.dumps(value_obj, indent=2))
    result_obj = []
    for stat in value_obj:
      result_obj.append({ "base_stat": stat['base_stat'], "stat_name": stat['stat']['name']})
      
    logging.debug("Transformed stats\n%s", json.dumps(result_obj, indent=2))
    return result_obj
  def helper_transform_types(value_obj):
    types_obj = []
    for type in value_obj:
      types_obj.append({ "slot": type['slot'], "type_name": type['type']['name']})
    
    return types_obj