import sys
import re

pattern = r"cat"

# чтобы считать все данные не зная сколько их будет
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) >= 2:
        print(line)
    if line == "":
        break








