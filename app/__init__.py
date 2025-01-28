from flask import Flask

from .routes import checker_routes

def create_app():
    app = Flask(__name__)

    app.register_blueprint(checker_routes.bp)

    return app