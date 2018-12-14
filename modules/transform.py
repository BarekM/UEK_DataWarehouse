import json
import config
import glob
from modules.helpers import read_json, write_json, get_from_dict, add_to_dict

def data_transform():
    
    try:

        files_list = glob.glob('{0}\\*.json'.format(config.path_scraped))
        all_files = len(files_list)
        file_counter = 0
        
        for file_path in files_list:
            try:
                dict_file = read_json(file_path)

                offer_id = get_from_dict('ID', dict_file)
                offer_type = get_from_dict('Rodzaj nieruchomoci', dict_file).lower()
                city = get_from_dict('Lokalizacja', dict_file)
                price = get_from_dict('Cena', dict_file).replace('z','').lower().strip()
                if not price.isnumeric():
                    price = ''
                rooms = get_from_dict('Liczba pokoi', dict_file).split(' ')[0].strip()
                if rooms == 'Kawalerka':
                    rooms = '1'
                elif int(rooms) > 5:
                    rooms = '5<'
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

                write_json(config.path_transformed + '\\' + offer_id + '.json', transformed_dict)

                file_counter += 1
            except Exception:
                pass
        message = '{0} out of {1} files transformed.'.format(file_counter, all_files)
        exit_code = 0
    
    except Exception as e:
        exit_code = 1
        message = str(e)
    
    status = (exit_code, message)
    return status
