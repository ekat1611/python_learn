from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests


url = input()
page = requests.get(url, verify=False)
soup = BeautifulSoup(page.text, "html.parser")

lst = []
# получить все теги <a> с html-страницы и пройтись по ним в цикле
for link in soup.find_all('a'):
    # Urlparse принимает адрес ссылки и делит её на 6 разных частей (протокол, хост и т.д.). нас интересует имя хоста
    link = urlparse(link.get('href')).hostname
    # если имя хоста невозможно "вычленить", то urlparse возвращает None
    if link not in lst and link is not None:
        lst.append(link)

lst = sorted(lst)

for _ in lst:
    print(_)