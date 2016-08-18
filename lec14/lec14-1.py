import requests

url = input('Input URL: ')
result = requests.get(url)
result.raise_for_status()

name = input('input filename: ')
file = open(name,'wb')
for chunk in result.iter_content(102400):
    file.write(chunk)

file.close()