import json
import os
import glob

import config


def read_json(path):
    with open(file=path, mode='r', encoding='ASCII', errors='ignore') as f:
        body = json.load(f)
        return body


def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)


def write_pretty_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def dict_to_string(my_dict):
    out_str = ', '.join('"{}"'.format(str(val)) for key, val in my_dict.items())
    out_str = out_str.replace('""', 'NULL')
    return out_str


def clear_directory(path_dir):
    files_list = glob.glob('{0}\\*'.format(path_dir))
    for file in files_list:
        os.remove(file)


def clear_temp_directories():
    clear_directory(config.path_scraped)
    clear_directory(config.path_transformed)
    clear_directory(config.path_print)
