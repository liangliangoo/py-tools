import json

import np as np


class Response(json.JSONEncoder):
    code = 10000
    msg = "success"
    data = None

    def __init__(self, code, msg, data):
        self.code = code
        self.msg = msg
        self.data = data

    @staticmethod
    def success(code, msg, data):
        return Response(code, msg, data)

    # @staticmethod
    # def success(msg):
    #     return Response(10000, msg, None)

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(Response, self).default(obj)
