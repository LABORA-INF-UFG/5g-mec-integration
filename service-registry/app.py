from flask  import Flask

from registry.registry import service_registry
from validateServer.test import sr_test
import config.config
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
import registry

def create_app():
   
    app = Flask(__name__)

    registry.init_app(app)
 
    app.register_blueprint(service_registry)
    app.register_blueprint(sr_test)
    app.config["JWT_SECRET_KEY"] = "ufg-br"
    jwt = JWTManager(app)
    
    return app