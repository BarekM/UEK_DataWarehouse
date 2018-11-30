import json


def read_json(path):
    with open(file=path, mode='r') as file:
        body = json.load(file)
        return body

