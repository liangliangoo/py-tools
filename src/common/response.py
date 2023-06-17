import json

import jsonpickle
import np as np


class Response(json.JSONEncoder):

    def __init__(self, code, msg, data):
        self.code = code
        self.msg = msg
        self.data = data

    @staticmethod
    def success(data):
        return jsonpickle.encode(Response(10000, "success", data), keys=True)

    @staticmethod
    def fail(data):
        return jsonpickle.encode(Response(20000, "fail", data))
