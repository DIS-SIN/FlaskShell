from flask import Flask

def register_view_routes(app: Flask) -> None:
    """Use this function to register routes"""

    from .hello_world.hello_world import hello_world_bp

    app.register_blueprint(hello_world_bp)
    app.add_url_rule('/', endpoint ="hello_world.hello_world")