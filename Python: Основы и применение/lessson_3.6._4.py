from xml.etree import ElementTree
results = {"red": 0, "green": 0, "blue": 0}

root = ElementTree.fromstring(input())


def parse_element(elem, lvl):
    lvl += 1
    results[elem.get("color")] += lvl
    for child in elem:
        parse_element(child, lvl)


parse_element(root, 0)

for key in results:
    print(results[key], end=' ')