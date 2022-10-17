from bs4 import BeautifulSoup
import requests



url = "https://vvsprogramm.github.io/B/"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "html.parser")

quote_elem = soup.find("p", class_="ieks-teksts")

quote_elem = quote_elem.get_text()
print(quote_elem)