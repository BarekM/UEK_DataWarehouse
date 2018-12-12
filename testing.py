import modules.load
from modules.load import load_files, output_db, clear_db, output_files
from modules.helpers import write_json, read_json
import config

import datetime

import glob



# path = 'xD.json'
#
# out = read_json(path)
# print(out)

#
# print(glob.glob(config.path_transformed + "\\*.json"))
#
# for idx in range(0,10):
#     myDict = {
#         'id': idx,
#         'type': 'pokoj',
#         'city': 'Krakow',
#         'price': '11111',
#         'rooms': '4',
#         'size': '50',
#         'parking': '',
#         'animal': '',
#         'smoking': '',
#         'renting': 'agencja',
#         'date_added': str(datetime.datetime.utcnow())
#     }
#     write_json('{0}\\{1}.json'.format(config.path_transformed, idx), myDict)
#
#
# load_files()
# print(output_db())
# clear_db()


output_files()

