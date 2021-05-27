import sys
from configparser import ConfigParser
from os import path

import yaml
from marshmallow import Schema, fields


def relative(filename):
    """Construct a path to filename relative
    to this file.
    """

    return path.join(path.dirname(__file__), filename)


class DBSectionSchema(Schema):
    db_url = fields.Str(required=True)


class AppSectionSchema(Schema):
    debug_host = fields.Str(default='localhost')
    debug_port = fields.Int(default=5000)
    secret_key = fields.Str(required=True)


SWAGGER_NAME = 'swagger.yaml'
SWAGGER_FILE = relative(SWAGGER_NAME)
try:
    with open(SWAGGER_FILE) as f:
        SWAGGER_CONFIG = yaml.safe_load(f)
except OSError:
    print('Error loading swagger configuration from {}'.format(SWAGGER_FILE))
    sys.exit(1)

CONFIG_NAME = 'config.ini'
CONFIG_FILE = path.join(path.dirname(__file__), CONFIG_NAME)

config = ConfigParser()
config.read(CONFIG_NAME)
db = DBSectionSchema().load(config['db'])
app = AppSectionSchema().load(config['app'])

DATABASE_URL = db['db_url']

DEBUG_HOST = app['debug_host']
DEBUG_PORT = app['debug_port']
SECRET_KEY = app['secret_key']
