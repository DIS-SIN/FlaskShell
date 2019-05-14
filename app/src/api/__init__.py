
from flask import Flask
from .apiV1_0 import register_api_routes_v1
def register_api_routes(app: Flask):
    """ use this function to register api routes"""
    # register the api versions to the main application 
    app.register_blueprint(register_api_routes_v1(latest = True))