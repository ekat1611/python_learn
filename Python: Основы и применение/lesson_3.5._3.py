import requests
import sys

url = 'http://numbersapi.com/'

with open("/Users/user/Downloads/dataset_24476_3.txt", "r") as numbers:
    for number in numbers.readlines():
        response = requests.get(url + number.rstrip() + '/math?json=true').json()
        if response.get('found', True):
            print('Interesting')
        else:
            print('Boring')
