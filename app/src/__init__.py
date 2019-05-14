from flask import Flask
from flask_cors import CORS

def create_app(mode="production",
               static_path="./static",
               templates_path="./templates",
               instance_path="./instance") -> Flask:
    import os
    from .utils.verify_user_constraints import verify
    from warnings import warn
    from werkzeug.utils import ImportStringError
    app = Flask(__name__)
    CORS(app)
    # configuring application
    app.config.from_object("configs.default_settings")

    if mode == "development":
        app.config.from_object("configs.development_settings")
    else:
        if mode != "production":
            warn("FLASK_ENV was set as an unrecognized value, " +
                 "application is falling back on production mode")
        try:
            app.config.from_object("configs.production_settings")
        except ImportStringError:
            pass

    # call in the verify function to validate application configuration
    verify(app)

    # If the secret key is none or the mode is production then we need to get the secret key from an environment variable
    if app.config.get('SECRET_KEY') is None or mode == "production":
        if os.environ.get("APP_SECRET_KEY") is None:
            if mode == "production":
                raise ValueError(
                    "APP_SECRET_KEY must be set as an environment " +
                    "variable for production environments")
            else:
                raise ValueError(
                    "SECRET_KEY was not set in the settings thus must be " +
                    "provided in the APP_SECRET_KEY environment variable")
        app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']
    # if the environment variable is not none we overide any configuration
    elif os.environ.get('APP_SECRET_KEY') is not None:
        app.config['SECRET_KEY'] = os.environ['APP_SECRET_KEY']

    # for database uri if there is a database
    """
    if app.config.get("DATABASE_URI") is None or mode == "production":
        if os.environ.get('APP_DATABASE_URI') is None:
            if mode == "production":
                raise ValueError(
                    "APP_DATABASE_URI must be set as an " +
                    "environment variable for production environments")
            else:
                raise ValueError(
                    "DATABASE_URI was not set in the settings " +
                    "thus must be provided in the " +
                    "APP_DATABASE_URI environment variable")

        app.config['DATABASE_URI'] = os.environ['APP_DATABASE_URI']
    elif os.environ.get("APP_DATABASE_URI") is not None:
        app.config['DATABASE_URI'] = os.environ['APP_DATABASE_URI']
    """

    # getting the absolute value for the static_path, template_path and instance_path
    if not os.path.isabs(static_path):
        static_path = os.path.abspath(static_path)
    if not os.path.isdir(static_path):
        raise FileNotFoundError(
            f'static folder was not able to be found {static_path}'
        )

    app.static_folder = static_path

    if not os.path.isabs(templates_path):
        templates_path = os.path.abspath(templates_path)
    if not os.path.isdir(templates_path):
        raise FileNotFoundError('templates folder was not able to be found')

    app.template_folder = templates_path

    if not os.path.isabs(instance_path):
        instance_path = os.path.abspath(instance_path)
    if not os.path.isdir(instance_path):
        os.mkdir(instance_path)

    app.instance_path = instance_path
    
    from src.database.db import init_app, distroy_db, init_db
    # initialise the app-database configurations
     
    init_app(app)

    from src.api import register_api_routes
    
    # register the api routes
    register_api_routes(app)

    from src.views import register_view_routes

    # register the view routes
    register_view_routes(app)
    
    # you can register some cli commands to be used with the flask command
    """
    @app.cli.command("init-db")
    def initialise_database():
        init_db(app)

    @app.cli.command("teardown-db")
    def distroy_database():
        distroy_db(app)
    """
    return app
