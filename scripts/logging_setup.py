import logging
from logging import handlers
from logging.handlers import RotatingFileHandler
import sys

# reroute python print() to logging framework
print = logging.info

logPath = './logs/'
fileName = 'debug'

# set handlers to print to both console and to a file
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName), 'w+')
consoleHandler.setLevel(logging.DEBUG)
# fileHandler = handlers.RotatingFileHandler("{0}/{1}.log".format(logPath, fileName), maxBytes=(1048576 *5), backupCount=7)

# add a command line argument here at some point
loggingHandlers = []
outputToFileAndConsole = True
if outputToFileAndConsole: 
  loggingHandlers.append(consoleHandler)
  loggingHandlers.append(fileHandler)
else:
  loggingHandlers.append(fileHandler)

# actual configs to logging
logging.basicConfig(
  format='%(asctime)s - %(levelname)-6s - %(message)s', 
  # filename="example.log", 
  # level=logging.DEBUG, 
  level=logging.DEBUG, 
  datefmt='%m/%d/%Y %I:%M:%S %p',
  handlers=loggingHandlers
)