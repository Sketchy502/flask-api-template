from flask import Flask, Response

from application.responses import ApiResponse


class ApiFlask(Flask):
    def make_response(self, rv) -> Response:
        if isinstance(rv, ApiResponse):
            return rv.to_response()
        return Flask.make_response(self, rv)


def create_app() -> ApiFlask:
    app = ApiFlask(__name__)

    return app
