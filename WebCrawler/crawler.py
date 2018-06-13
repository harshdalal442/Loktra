# Web Crawler

from bs4 import BeautifulSoup
import requests
import sys


def crawl_keyword(keyword):
	print(keyword)	
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
