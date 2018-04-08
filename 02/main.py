import requests
from bs4 import BeautifulSoup




def get_html(url):
	r = requests.get(url)
	return r.text


def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	news = soup.find_all('div', class_='sh_art')

	for n in news:
		title = n.find('h2').find('u').text.strip()
		url = n.find('h2').find('a').get('href')
		snippet = n.find('p').text.strip()
		print(url)



	#return news


def main():
	url = 'https://footballhd.ru/allnews/'
	print(get_data(get_html(url)))
	






if __name__ == '__main__':
	main()