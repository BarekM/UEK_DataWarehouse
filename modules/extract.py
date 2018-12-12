from bs4 import BeautifulSoup
import requests
import json
import config


def data_scrape(city):
    
    try:
        
        page_counter = 0
        current_page = ''
        previous_page = ''
        
        for page in range(1, config.pages_limit):
       
            url = 'https://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/' + city + '/page-' + str(page) + '/' + config.dict_city[city] + str(page)
            page_response = requests.get(url)
            page_content = BeautifulSoup(page_response.content, 'lxml')
        
            current_page = page_content.find('span', class_ = 'current').text.strip()
          
            if current_page != previous_page:
                
                single_offer_urls = page_content.find_all('a', class_ = 'href-link')
        
                for single_url_full in single_offer_urls:
                    single_url ='https://www.gumtree.pl' + single_url_full.get('href')
                    unique_id = single_url.split('/')[-1]
                    
                    single_page_response = requests.get(single_url)
                    single_page_content = BeautifulSoup(single_page_response.content, 'lxml')
            
                    price = single_page_content.find('div', class_= 'price').text.strip()
                    single_page_dict = {'ID': unique_id, 'Cena': price}
            
                    details = single_page_content.find_all('div', class_ = 'attribute')
             
                    for detail in details:
                        detail_name = detail.find('span', class_ = 'name').text.strip()
                        detail_value = detail.find('span', class_ = 'value').text.strip()
                        
                        single_page_dict[detail_name] = detail_value
                       
                    with open(config.path_scraped + '\\' + unique_id + '.json', 'a', encoding = 'utf-8') as text_file:
                        text_file.write(json.dumps(single_page_dict, ensure_ascii = False))
                        
                previous_page = current_page
                page_counter += 1
                
            else: break
        
        message = '{0} out of {1} pages extracted.'.format(page_counter, config.pages_limit)
        exit_code = 0
    
    except Exception as e:
        exit_code = 1
        message = str(e)
        
    status = (exit_code, message)
    return status
