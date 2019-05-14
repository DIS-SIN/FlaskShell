from flask import Blueprint
from flask_restful import Api
def register_api_routes_v1(latest: bool) -> Blueprint:
    """use this function to register api routes"""
    
    # create blueprint and instatiate the Api on the blueprint
    api_bp = Blueprint('apiV1_0', __name__)
    if latest:
        # if the application is the latest then load it under the url prefix /api
        api = Api(api_bp, prefix='/api')
    else:
        # otherwise load it under /api and its routes
        api = Api(api_bp, prefix='/api/V1_0')
    
    from .resources.hello_world import HelloWorld
    api.add_resource(HelloWorld, '/helloWorld', endpoint='hello_world')

    # return the blueprint
    return api_bp
        
    
