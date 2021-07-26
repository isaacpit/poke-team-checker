import sys
import pprint as pp
from typing import Type

import requests
import json

import logging 

from logging_setup import *

# print = logging.info


class PokeApiGenerator:
  POKE_API_BASE_URL = "https://pokeapi.co/api/v2/"
  GET_ALL_POKEMON_URL = POKE_API_BASE_URL + "pokemon"
  KEY_URL = 'url'

  def get_pokemon_w_limit_query_url(limit: int) -> str:
    logging.info("Getting pokemon with limit: {}".format(limit))
    return PokeApiGenerator.GET_ALL_POKEMON_URL + "?limit=" + str(limit)

  def loopThroughList(pokeResultsList):
    for getPokeListResult in pokeResultsList:
      PokeApiGenerator.validateGetPokemonApiResponse(getPokeListResult)
        

      a_pokemon_url = getPokeListResult['url']
      logging.info("calling pokeApi with url: {}".format(a_pokemon_url))
      response = requests.get(a_pokemon_url)
      logging.info("\n{}".format(pp.pformat(list(response.json().keys()))))
      extractedObj = PokemonInfoResponse(response.json())
      logging.info(json.dumps(extractedObj.d_data, indent=2))

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
    for k, v in response_obj.items():
      print("{:30} {:20} {:10}".format(k, str(v)[0:20], k in PokemonInfoResponse.DESIRED_FIELDS))
      if k in PokemonInfoResponse.DESIRED_FIELDS:
        self.d_data[k] = PokemonInfoResponse.transform_data(k, v)

    logging.info(json.dumps(self.d_data, indent=2))
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
    print(json.dumps(value_obj, indent=2))
    result_obj = []
    for stat in value_obj:
      result_obj.append({ "base_stat": stat['base_stat'], "stat_name": stat['stat']['name']})
      
    print(result_obj)
    return result_obj
  def helper_transform_types(value_obj):
    types_obj = []
    for type in value_obj:
      types_obj.append({ "slot": type['slot'], "type_name": type['type']['name']})
    
    return types_obj