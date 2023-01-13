import requests
import re

link1, link2 = input(), input()
# в случае если в html файле несколько ссылок, то данный паттерн должен искать "неладным" способом: +?
# в противном случае, будет отдаваться весь контент от начала первой ссылки https:// и до конца последней html
pattern = r'https://.+?html'

response = str(requests.get(link1).content)

link_lst = re.findall(pattern, response)
for i in range(len(link_lst)):
    response1 = requests.get(link_lst[i])
    if link2 in str(response1.content):
        print('Yes')
        break
else:
    print('No')