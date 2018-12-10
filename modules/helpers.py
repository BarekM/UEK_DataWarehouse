import json


def read_json(path):
    with open(file=path, mode='r') as f:
        body = json.load(f)
        return body


def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)

