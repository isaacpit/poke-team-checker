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



LIMIT = 2

logging.basicConfig(format='%(asctime)s - %(levelname)-10s - %(message)s', filename="example.log", level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')
# logger= logging.getLogger("data_gen.py")



url = PokeApiGenerator.get_pokemon_w_limit_query_url(LIMIT)
logging.info("calling pokeApi with url: {}".format(url))
response = requests.get(url)

responseObj = json.loads(response.content)
logging.info("response {}".format("-" * 20))
# pp.pprint(responseObj, indent=1)

pokeResultsList = responseObj["results"]
logging.info("pokeResultsList: {}".format( "-" * 20))
for x in pokeResultsList:
  # pp.pprint(x)
  logging.info(pp.pformat(x))
# pp.pprint(pokeResultsList)



PokeApiGenerator.loopThroughList(pokeResultsList)
