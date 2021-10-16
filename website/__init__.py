from flask import Flask
from os import pathsep


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "weLiveInASociety"

    from .views import views
    
    app.register_blueprint(views, url_prefix="/")

    return app