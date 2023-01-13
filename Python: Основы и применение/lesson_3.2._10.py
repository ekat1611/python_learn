import sys
import re

pattern = r".*\\.*"

for line in sys.stdin:
    if re.search(pattern, line):
        print(line, end = "")