import json
import os
import glob

import config


def get_filename(path):
    file_name = path.split('\\')[-1]
    return file_name


def read_json(path):
    with open(file=path, mode='r', encoding='ASCII', errors='ignore') as f:
        body = json.load(f)
        return body


def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, ensure_ascii=False)


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
        try:
            os.remove(file)
        except PermissionError:
            pass

def clear_temp_directories():
    clear_directory(config.path_scraped)
    clear_directory(config.path_transformed)
    clear_directory(config.path_print)


def get_from_dict(dict_key, dict_name):
    if dict_key in dict_name:
        dict_value = dict_name[dict_key]
    else:
        dict_value = ''
    return(dict_value)


def add_to_dict(dict_key, dict_value, dict_name):
    dict_name[dict_key] = dict_value
