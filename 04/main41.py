import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)    
    

def write_csv(data):
    with open('yaca.csv', 'a') as f:
        writer = csv.writer(f
        pass
        

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')


def main():
    url = 'https://yandex.ua/yaca/cat/Sports/Football/1.html'
    get_html(url)
    

if __name__ == '__main__':
    main()