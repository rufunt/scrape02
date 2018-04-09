import requests
from bs4 import BeautifulSoup
import csv




def get_html(url):
	r = requests.get(url)
	return r.text

def write_csv(data):
	with open('cmc.csv', 'a') as f:
		writer = csv.writer(f)

		writer.writerow((data['title'], data['snipet'], data['url'] ))
		




def main():
	url = 'https://coinmarketcap.com/'
	
	



if __name__ == '__main__':
	main()