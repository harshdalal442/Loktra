# Web Crawler
from bs4 import BeautifulSoup
import requests
import sys

def generate_url(keyword, page_number=None):
	if page_number is not None:
		return 'http://www.shopping.com/products~PG-'+page_number+'?KW='+keyword
	else:
		return 'http://www.shopping.com/products?KW='+keyword

def get_html(url):
	response = requests.get(url)
	if (response.status_code == 200):
		return response.text
	else:
		print("Server under maintenance.! Please try again later")

def crawl_keyword(keyword):
	html = get_html(generate_url(keyword))	
	return keyword

def crawl_keyword_page(keyword, page_number):
	print(keyword, page_number)
	return (keyword, page_number)

if len(sys.argv) == 2:
	crawl_keyword(sys.argv[1])
elif len(sys.argv) == 3:
	crawl_keyword_page(sys.argv[1], sys.argv[2])
else:
	print("Please run the code using one of the below:\n  --> python crawler.py <keyword> \n  --> python crawler.py <keyword> <page number>")