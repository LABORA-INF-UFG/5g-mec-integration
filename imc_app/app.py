from flask import Flask, request

from imc_calc.imc_calc import imc_calc

imcResults = []

def create_app():
    from registry import requestRegistry
    app = Flask(__name__)
    requestRegistry.make_registry(app)
    app.register_blueprint(imc_calc)
    return app
    
    