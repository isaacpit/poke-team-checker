from logging import log
import sys
import requests
import pprint as pp 
import json

# import logging
# overrides python's print() to point to logger
from logging_setup import *

import time
from threading import Thread

# import http.client

# httpclient_logger = logging.getLogger("http.client")

# def httpclient_logging_patch(level=logging.DEBUG):
#     """Enable HTTPConnection debug logging to the logging framework"""

#     def httpclient_log(*args):
#         httpclient_logger.log(level, " ".join(args))

#     # mask the print() built-in in the http.client module to use
#     # logging instead
#     http.client.print = httpclient_log
#     # enable debugging
#     http.client.HTTPConnection.debuglevel = 1

# httpclient_logging_patch()
from PokeApiGenerator import PokeApiGenerator, PokemonInfoResponse

LIMIT = 1200
# logger= logging.getLogger("data_gen.py")

url = PokeApiGenerator.get_pokemon_w_limit_query_url(LIMIT)
logging.debug("calling pokeApi with url: {}".format(url))
response = requests.get(url)

responseObj = json.loads(response.content)
# pp.pprint(responseObj, indent=1)

pokeResultsList = responseObj["results"]
for x in pokeResultsList:
  # pp.pprint(x)
  logging.debug(pp.pformat(x))
# pp.pprint(pokeResultsList)



pokeResultsList = PokeApiGenerator.loopThroughList(pokeResultsList)

pokemonOutputRelativePath = '../data/'
pokemonOutputFileName = 'poke-data.json'
pokemonOutputFullName = pokemonOutputRelativePath + pokemonOutputFileName
prettyOutput = True
# print("POKE-RESULTS: {}".format(pokeResultsList))
print("outputting to file: {}".format(pokemonOutputFileName))
with open(pokemonOutputFullName, 'w') as f:
  if prettyOutput:
    json.dump(pokeResultsList, f, indent=2)
  else:
    json.dumps(pokeResultsList, f)


