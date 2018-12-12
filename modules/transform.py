import json
#import config
import glob

def read_json(path):
    with open(file=path, mode='r', encoding='ASCII', errors='ignore') as f:
        body = json.load(f)
        
        return body

def get_from_dict(dict_key, dict_name):
    if dict_key in dict_name:
        dict_value = dict_name[dict_key]
    else:
        dict_value = ''
    return(dict_value)

def city_adjust(city):
    city_mapping = {'Krakw': 'Krakow', 'Wrocaw': 'Wroclaw', 'Gdask': 'Gdansk', 'Pozna': 'Poznan', 'd': 'Lodz', 'Rzeszw': 'Rzeszow'}
    return(city_mapping[city])
    
def add_to_dict(dict_key, dict_value, dict_name):
    dict_name[dict_key] = dict_value
                       
def data_transform():
    
    try:
        
        files_list = glob.glob('{0}\\*.json'.format('Temp\\extracted'))
        #files_list = glob.glob('{0}\\*.json'.format(config.path_scraped))
        all_files = len(files_list)
        file_counter = 0
        
        for file_path in files_list:
            dict_file = read_json(file_path)
            
            offer_id = get_from_dict('ID', dict_file)
            offer_type = get_from_dict('Rodzaj nieruchomoci', dict_file).lower()
            city = get_from_dict('Lokalizacja', dict_file).split(',')[0].strip()
            city = city_adjust(city)
            price = get_from_dict('Cena', dict_file).replace('z','').lower().strip()
            rooms = get_from_dict('Liczba pokoi', dict_file).split(' ')[0].strip()
            size = get_from_dict('Wielko (m2)', dict_file)
            parking = get_from_dict('Parking', dict_file).lower()
            if parking != 'brak' and parking != 'garaz' and parking != 'ulica':
                parking = ''
            animal = get_from_dict('Przyjazne zwierzakom', dict_file).lower()
            smoking = get_from_dict('Palcy', dict_file).lower()
            renting = get_from_dict('Do wynajcia przez', dict_file).lower().replace('waciciel', 'wlasciciel')
            date_added = get_from_dict('Data dodania', dict_file)
            
            transformed_dict = {}
            add_to_dict('id', offer_id, transformed_dict)
            add_to_dict('type', offer_type, transformed_dict)
            add_to_dict('city', city, transformed_dict)
            add_to_dict('price', price, transformed_dict)
            add_to_dict('rooms', rooms, transformed_dict)
            add_to_dict('size', size, transformed_dict)
            add_to_dict('parking', parking, transformed_dict)
            add_to_dict('animal', animal, transformed_dict)
            add_to_dict('smoking', smoking, transformed_dict)
            add_to_dict('renting', renting, transformed_dict)
            add_to_dict('date_added', date_added, transformed_dict)
            
            #print(offer_id, offer_type, city, price, rooms, size, parking, animal, smoking, renting, date_added)
            with open('Temp\\transformed\\' + offer_id + '.json', 'a', encoding = 'utf-8') as text_file:
                        text_file.write(json.dumps(transformed_dict))
                        
            file_counter += 1
        message = '{0} out of {1} files transformed.'.format(file_counter, all_files)
        exit_code = 0
    
    except Exception as e:
        raise
        exit_code = 1
        message = str(e)
    
    status = (exit_code, message)
    return status

print(data_transform())