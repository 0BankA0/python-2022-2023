import requests
from bs4 import BeautifulSoup

Web_url = "https://vvsprogramm.github.io/2021_debug/"

r = requests.get(Web_url)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())