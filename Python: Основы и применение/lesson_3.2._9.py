import sys
import re

pattern = "z.{3}z"

for line in sys.stdin:
    if re.search(pattern, line):
        print(line, end = "")