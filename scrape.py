import requests
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from requests_html import HTMLSession


baseurl = 'https://www.traderjoes.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}


# def render_page(url):
#   driver = webdriver.Chrome(options=options)
#   driver.get(url)
#   time.sleep(3)
#   r = driver.page_source
#   return r

queries = ['eggs', 'cookies']
for query in queries:
  url = f'{baseurl}/home/search?q={query}&section=products&global=yes'
  session = HTMLSession()
  response = session.get(url)
  response.html.render(sleep=1.5)

  soup = bs(response.html.html, 'html.parser')
  # soup = bs(page, 'html.parser')
  results = soup.find_all(class_='SearchResultCard_searchResultCard__3V-_h')

  for item in results:
    name = item.h3.text
    price = item.find(class_='ProductPrice_productPrice__price__3-50j').text
    print(f'{name} --  {price}')

  # print(results)
