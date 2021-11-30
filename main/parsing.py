import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    response = requests.get(url, headers=headers)
    return response.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_list = soup.find('div', class_="section-9-list")
    products = product_list.find_all('section', class_="section-9-itm")
    list_ = []
    for product in products:
        title = product.find('h3', class_="section-9-title").find('a').text
        description = product.find('div', class_="section-9-descr").text
        data = {'title': title, 'description': description}
        list_.append(data)
    return list_


def main():
    url = 'https://viva.ua/all'
    l = get_html(url)
    k = get_page_data(l)
    return k


