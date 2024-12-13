import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import json

saber_pars = []
def saber(catagory):
    load_dotenv()
    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0'
    }

    saber_pars.clear()



    response = requests.get(URL + catagory, headers=HEADERS).text
    soup = BeautifulSoup(response, 'html.parser')
    blocks = soup.find_all('div', class_='col-12 col-sm-6 col-lg-4')


    for block in blocks:
        images = block.find('img').get('src')
        title = block.find('h4').get_text()
        products = block.find('ul', class_='product__single-text-categories').get_text(strip=True)
        many = block.find('span').get_text(strip=True)
        link = HOST + block.find('a').get('href')

        saber_pars.append({
            'images': images,
            'title': title,
            'products': products,
            'many': many,
            'link': link
        })
    return saber_pars





saber('category/49')