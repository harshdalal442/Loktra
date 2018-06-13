# Web Crawler
from bs4 import BeautifulSoup
import requests
import sys

def get_maximum_number(input_query):	
	max = -9
	for word in input_query.split(" "):		
		if word.strip().isdigit():
			if int(word.strip()) > max:
				max = int(word.strip())
	return max

def generate_url(keyword, page_number=None):
	if page_number is not None:
		return 'http://www.shopping.com/products~PG-'+page_number+'?KW='+keyword
	else:
		return 'http://www.shopping.com/products?KW='+keyword

def parse_html(response):
	soup = BeautifulSoup(response, "html.parser")
	spans = soup.find_all('span', attrs={'class':'numTotalResults'})
	return ("".join(spans[0].strings))

def get_html(url):
	response = requests.get(url)	
	if (response.status_code == 200):
		return response.text
	else:
		print("Server under maintenance.! Please try again later")

def crawl_keyword(keyword):
	html = get_html(generate_url(keyword))	
	print("Number of total results for "+keyword+" are: ", get_maximum_number(parse_html(html)))

def crawl_keyword_page_number(keyword, page_number):
	html = get_html(generate_url(keyword, page_number))	
	return (keyword, page_number)

if len(sys.argv) == 2:
	crawl_keyword(sys.argv[1])
elif len(sys.argv) == 3:
	crawl_keyword_page_number(sys.argv[1], sys.argv[2])
else:
	print("Please run the code using one of the below:\n  --> python crawler.py <keyword> \n  --> python crawler.py <keyword> <page number>")