import requests
from bs4 import BeautifulSoup

res = requests.get('https://tocknicsu.mzshieh.io/snp2016/html/3.html')

soup = BeautifulSoup(res.text, 'lxml')

div_id = soup.find('div', id="find_by_id")
print(div_id)

div_id = soup.find('div', {'id': 'find_by_id'})
print(div_id)

# cannot do this
# div_class = soup.find('div', class='find_by_class')
# print(div_class)

div_class = soup.find('div', {'class': 'find_by_class'})
print(div_class)


