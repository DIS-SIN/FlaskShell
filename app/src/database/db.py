from flask import current_app, g, Flask
from src.models import init_base
from neomodel.util import Database


def get_db() -> Database:
    """
    Get the loaded db object from neomodel
    """
    pass


def close_db(e=None):
    """
    Used to close the session and end the connection between the database
    and the client
    """
    pass


def init_app(app: Flask):
    # register the close_db with the removal of the app context event
    app.teardown_appcontext(close_db)
    # init_base is used to initialise the NeoModel config
    init_base(app)


def init_db(app):
    from .utils.detect_loaders import detect
    import importlib
    try:
        loaders = importlib.import_module('src.database.loaders')
        mods = detect(loaders)
        for mod in mods:
            mod_obj = getattr(loaders, mod)
            run_method = getattr(mod_obj, 'run')
            run_method(app)
    except ImportError:
        pass


def distroy_db(app):
    """
    wipe the database
    """
    pass 