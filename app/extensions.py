from flasgger import Swagger
from flask_httpauth import HTTPBasicAuth
from flask_login import LoginManager
from flask_principal import Principal
from flask_restful import Api

from settings import SWAGGER_CONFIG

api = Api()
flask_httpauth = HTTPBasicAuth()
flask_principal = Principal()
swagger = Swagger(config=SWAGGER_CONFIG, merge=True)
login_manager = LoginManager()
