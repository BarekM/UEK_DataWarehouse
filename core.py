import modules.load
from modules.load import DatabaseConnection, load_files, output_db
from modules.helpers import write_json
import config

import datetime

import glob

# print(glob.glob(config.path_transformed + "\\*.json"))
#
# for idx in range(0,10):
#     myDict = {
#         'id': idx,
#         'name': 'xD',
#         'type': 'pokoj',
#         'city': 'Krakow',
#         'price': '11111',
#         'rooms': '4',
#         'size': '50',
#         'parking': 'brak',
#         'animal': '',
#         'smoking': '',
#         'renting': 'agencja',
#         'date_added': str(datetime.datetime.utcnow())
#     }
#     write_json('{0}\\{1}.json'.format(config.path_transformed, idx), myDict)
#
# dbc = DatabaseConnection()
# dbc.clear_database()
# load_files()
output_db()

