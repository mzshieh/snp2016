import requests
from bs4 import BeautifulSoup

res = requests.get('https://mzshieh.github.io/snp2016/html/5.html')

soup = BeautifulSoup(res.text, 'lxml')

divs = soup.find_all('div')
print(divs)

print("=====")

outter = soup.find('div', {'class': 'outer'})
print(outter)

print("=====")

inner = outter.div
print(inner)

print("=====")

inner = outter.find('div', {'class': 'inner'})
print(inner)

