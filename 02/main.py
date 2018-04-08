import requests
from bs4 import BeautifulSoup
import csv




def get_html(url):
	r = requests.get(url)
	return r.text

def write_csv(data):
	with open('news.csv', 'a') as f:
	writer = csv.writer(f)

	writer.writerow((data['title'], data['snipet'], data['url'] ))
		


def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	news = soup.find_all('div', class_='sh_art')

	for n in news:
		title = n.find('h2').find('u').text.strip()
		url = n.find('h2').find('a').get('href')
		snippet = n.find('p').text.strip()
		
		data = {'title': title, 'snipet': snipet, 'url': url}



	#return news


def main():
	url = 'https://footballhd.ru/allnews/'
	print(get_data(get_html(url)))
	






if __name__ == '__main__':
	main()