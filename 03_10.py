from bs4 import BeautifulSoup
import requests
 
def apstrada_lapu(url):
    r = requests.get(url) 
    html = r.text
    soup = BeautifulSoup(html, 'html.parser') 
    return soup
 
html = apstrada_lapu("https://www.tvnet.lv") 
print(html.head.title.text)
