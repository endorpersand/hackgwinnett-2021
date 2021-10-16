from flask import Flask
from os import pathsep


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "weLiveInASociety"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app


for i in range(68):
    x = 2
