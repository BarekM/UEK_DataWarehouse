import json


def read_json(path):
    with open(file=path, mode='r') as f:
        body = json.load(f)
        return body


def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)


def dict_to_string(my_dict):
    out_str = ', '.join('"{}"'.format(str(val)) for key, val in my_dict.items())
    out_str = out_str.replace('""', 'NULL')
    return out_str

