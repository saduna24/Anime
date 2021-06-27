import requests
from bs4 import BeautifulSoup
file = open('anime', 'w', encoding='UTF-8_sig', newline='\r\n')
file.write('სათაური\n')


resp = requests.get('https://animetv.night-city.online/top100.html')

content = resp.text

soup = BeautifulSoup(content, 'html.parser')

movie = soup.find_all('div', {'class': 'content'})

for each in movie:
    t = each.find('div', {'class': 'movie-item__title'})
    names = each.text.replace(' ', '')
    file.write(names + ',')




