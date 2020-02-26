from flask import Flask


class ApiFlask(Flask):
    pass


def create_app():
    app = ApiFlask(__name__)

    return app
