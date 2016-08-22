import requests
from bs4 import BeautifulSoup

res = requests.get('https://tocknicsu.github.io/snp2016/html/4.html')

soup = BeautifulSoup(res.text, 'lxml')

divs = soup.find_all('div')
print(divs)

