path_temp = r'F:\MyTemp\UekTemp'
path_scraped = '{0}\\{1}'.format(path_temp, 'extracted')
path_transformed = '{0}\\{1}'.format(path_temp, 'transformed')
path_processed = '{0}\\{1}'.format(path_temp, 'processed')
path_print = '{0}\\{1}'.format(path_temp, 'output')
path_print_files = '{0}\\{1}'.format(path_temp, 'output\\files')
path_errors = '{0}\\{1}'.format(path_temp, 'errors')

db_user = 'crawler'
db_password = 'admin'
db_host = 'localhost'
db_name = 'dev_uek_dw'

dict_city = {
  'Warszawa': 'v1c9008l3200008p',
  'Krakow': 'v1c9008l3200208p',
  'Wroclaw': 'v1c9008l3200114p',
  'Gdansk': 'v1c9008l3200072p',
  'Lublin': 'v1c9008l3200145p',
  'Poznan': 'v1c9008l3200366p',
  'Lodz': 'v1c9008l3200183p',
  'Katowice': 'v1c9008l3200285p',
  'Rzeszow': 'v1c9008l3200252p',
  'Szczecin': 'v1c9008l3200402p',
}

pages_limit = 15
