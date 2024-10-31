
import json


class JSONFormater():
    def __init__(self, data):
        self.data = data

    def format(self):
        return json.dumps(self.data, indent=4)

    def transformToData(self):
        return json.loads(self.data)

    def ObjectToData(obj):
        return json.dumps(obj.__dict__, indent=4)