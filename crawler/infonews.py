import requests
from bs4 import BeautifulSoup

res = requests.get('https://infonews.nctu.edu.tw', verify=False)
soup = BeautifulSoup(res.text, "lxml")

LIST = soup.find('div', id="layout_campu")
for x in LIST.find_all("td", {"class": "style2"}):
    print(x.encode('latin1').decode('big5', 'ignore'))


