import requests
from bs4 import BeautifulSoup




def get_html(url):
	r = requests.get(url)
	return r.text





def main():
	url = 'https://footballhd.ru/allnews/'
	






if __name__ == '__main__':
	main()