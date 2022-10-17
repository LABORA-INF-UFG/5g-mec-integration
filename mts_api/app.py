from flask import Flask
from dataManager.dataManager import dataM
from controller.mtsController import mtsController

def create_app():
    from registry import Registry    
    
    app = Flask(__name__)

    app.register_blueprint(dataM)
    app.register_blueprint(mtsController)
    
    Registry.make_registry(app)
    
    return app
