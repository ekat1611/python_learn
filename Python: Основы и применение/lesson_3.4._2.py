import csv
from collections import Counter
primary_types = []

with open("/Users/user/Downloads/Crimes.csv") as crimes:
    reader = csv.reader(crimes)
    test = csv.DictReader(crimes)
    for row in test:
        primary_types.append(row['Primary Type'])

test = Counter(primary_types)
for key in test:
    print(key)
    break