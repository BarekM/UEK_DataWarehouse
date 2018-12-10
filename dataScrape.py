# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 20:04:56 2018

@author: Monika
"""

from bs4 import BeautifulSoup
import requests
import json

city = 'krakow'
cityID = 'v1c9008l3200208p'
pagesNumber = int('10')

"""
url = 'https://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/' + city + '/page-' + str(1) + '/' + cityID + str(1)
pageResponse = requests.get(url)
pageContent = BeautifulSoup(pageResponse.content, 'lxml')
numberOfPages = pageContent.find('span', class_ = 'count').text.split(':')[1].strip()
print(numberOfPages)
"""
currentPage = ''
previousPage = ''

for page in range(1,pagesNumber):
    
    url = 'https://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/' + city + '/page-' + str(page) + '/' + cityID + str(page)
    pageResponse = requests.get(url)
    pageContent = BeautifulSoup(pageResponse.content, 'lxml')
    
    currentPage = pageContent.find('span', class_ = 'current').text.strip()
   
    print(currentPage + ' ' + previousPage)
    if currentPage != previousPage:
        """
        singleOfferUrls = pageContent.find_all('a', class_ = 'href-link')
    
        for singleUrlFull in singleOfferUrls:
            singleUrl = singleUrlFull.get('href')
            uniqueID = singleUrl.split('/')[-1]
            #print(uniqueID)
            singleUrl = 'https://www.gumtree.pl' + singleUrlFull.get('href')
            #print(singleUrl)
        
            singlePageResponse = requests.get(singleUrl)
            singlePageContent = BeautifulSoup(singlePageResponse.content, 'lxml')
        
            price = singlePageContent.find('div', class_= 'price').text.strip()
            singlePageDict = {'ID': uniqueID, 'Cena': price}
        
            details = singlePageContent.find_all('div', class_ = 'attribute')
         
            for detail in details:
                detailName = detail.find('span', class_ = 'name').text.strip()
                detailValue = detail.find('span', class_ = 'value').text.strip()
            
                singlePageDict[detailName] = detailValue
        
            with open('Temp\\Extracted\\' + uniqueID + '.json', 'a', encoding = 'utf-8') as text_file:
                text_file.write(json.dumps(singlePageDict, ensure_ascii = False))
                """
        previousPage = currentPage
        
    else: break