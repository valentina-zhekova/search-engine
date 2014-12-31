import requests
from bs4 import BeautifulSoup

r = requests.get('http://hackbulgaria.com')
html = r.text
soup = BeautifulSoup(html)

for link in soup.find_all('a'):
    print(link.get('href'))
