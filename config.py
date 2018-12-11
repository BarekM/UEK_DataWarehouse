path_temp = r'F:\MyTemp\UekTemp'
path_scraped = '{0}\\{1}'.format(path_temp, 'extracted')
path_transformed = '{0}\\{1}'.format(path_temp, 'transformed')
path_processed = '{0}\\{1}'.format(path_temp, 'processed')
path_print = '{0}\\{1}'.format(path_temp, 'output')

db_user = 'crawler'
db_password = 'admin'
db_host = 'localhost'
db_name = 'dev_uek_dw'

dict_city = {
  'warszawa': 'v1c2l3200008p',
	'krakow': 'v1c9008l3200208p',
	'wroclaw': 'v1c9008l3200114p',
	'gdansk': 'v1c9008l3200072p',
	'lublin': 'v1c9008l3200145p',
	'poznan': 'v1c9008l3200366p',
	'lodz': 'v1c9008l3200183p',
	'katowice': 'v1c9008l3200285p',
	'rzeszow': 'v1c9008l3200252p',
	'szczecin': 'v1c9008l3200402p',
}

pages_limit = '10'
