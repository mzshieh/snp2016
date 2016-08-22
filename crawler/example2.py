import requests
from bs4 import BeautifulSoup

res = requests.get('https://tocknicsu.github.io/snp2016/html/2.html')

soup = BeautifulSoup(res.text, 'lxml')

a = soup.find('a')
print(a)
print(a.text)

print(a.get('href'))
print(a['href'])

print(a.get('xd'))
print(a['xd'])
