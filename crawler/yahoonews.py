import requests
import random
from bs4 import BeautifulSoup
import os

try:
    os.makedirs('news')
except:
    pass

res = requests.get('https://tw.news.yahoo.com/sports/')
# soup = BeautifulSoup(res.text, "html.parser")
soup = BeautifulSoup(res.text, "lxml")

links = soup.select('a.title')
candidate_links = []
for x in links:
    if x.get('href').endswith('html'):
        candidate_links.append(x)

target_links = random.sample(candidate_links, 5)

base_url = "https://tw.news.yahoo.com"

for link in target_links:
    print('%s%s'%(base_url, link.get('href')))
    res = requests.get('%s%s'%(base_url, link.get('href')))
    soup = BeautifulSoup(res.text, 'lxml')
    content = soup.select('div#mediaarticlebody')
    content = content[0].select('p')
    f = open('news/%s'%(link.get('href')[1:]), 'w')
    for x in content:
        f.write(x.text)
    f.close()
    print(content)


