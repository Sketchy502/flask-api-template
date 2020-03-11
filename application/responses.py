import json
from http import HTTPStatus
from flask import Response


class ApiResponse:
    def __init__(self, value, status_code=HTTPStatus.OK):
        self.value = value
        self.status_code = status_code

    def to_json(self) -> str:
        return json.dumps(self.value)

    def to_response(self) -> Response:
        return Response(
            self.to_json(),
            status=self.status_code,
            mimetype="application/json"
        )
