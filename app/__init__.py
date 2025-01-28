from flask import Flask

from .routes import checker_routes

def create_app():
    app = Flask(__name__)

    return app