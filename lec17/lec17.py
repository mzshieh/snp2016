import requests, os, random
from bs4 import BeautifulSoup

# Dumping the result to file arg['dir']/name
def dump(result, name, **arg):
    if arg.get('dir')!=None:
        try:
            os.makedirs(arg['dir'])
            name = arg['dir']+'/'+name
        except:
            print('unable to use '+arg['dir'])
        file = open(name,'wb')
        for chunk in result.iter_content(102400):
            file.write(chunk)
        file.close()

# get
res = requests.get('https://tw.news.yahoo.com/sports/')

soup = BeautifulSoup(res.text, "lxml")
# if lxml does not work, uncomment the following
# soup = BeautifulSoup(res.text, "html.parser")

tag = soup.find('a')
print('The first <a> tag:',tag)

tags = soup.find_all('a')
print('There are',len(tags),'<a> tags.')

tags = soup.find_all('div',{'class':'txt'})
print('There are',len(tags),'<div> tags with class attribute "txt".')

tags = soup.select('a.title')
print('There are',len(tags),'<a> tags with class attribute "title".')

tags = soup.select('div#mediamegatron')
print('There are',len(tags),'<div> tags with id attribute "mediamegatron".')

# dump the result
dump(res,'raw',dir='tmp')
