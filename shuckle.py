#!/usr/bin/python3.5

from discord import Client
import os
import sys

from config import config
from secrets import secrets

if '--debug' in sys.argv:
    __DEBUG__ = True
elif '-d' in sys.argv:
    __DEBUG__ = True
else:
    __DEBUG__ = False

# Shuckle adds internal path variables to
# the config at runtime.
config.__BASE__ = os.path.abspath(os.path.dirname(__file__))
config.__MAIN__ = os.path.abspath(__file__)
config.__DATA__ = os.path.join(config.__BASE__, 'data')
config.__SHUCKLE__ = os.path.join(config.__BASE__, 'shuckle')
config.__BOTS__ = os.path.join(config.__BASE__, config.bots_folder)

sys.path.append(config.__SHUCKLE__)
sys.path.append(os.path.join(config.__SHUCKLE__, 'db'))

if __name__ == '__main__':
    print('Starting up...')
    print('Debug status: {}'.format(__DEBUG__))

    from shuckle.core import Toolbox

    client = Toolbox(debug=__DEBUG__)

    client.run(secrets.token)
