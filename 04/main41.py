import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)    
    

def write_csv(data):
    with open('websites.csv', 'a') as f:
        order = []
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)




def main():
    url = 'https://yandex.ua/yaca/cat/Sports/Football/1.html'
    

if __name__ == '__main__':
    main()