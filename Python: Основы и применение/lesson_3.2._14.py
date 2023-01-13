import sys
import re

pattern = r"\b(\w)(\w)"

for line in sys.stdin:
    print(re.sub(pattern, r"\2\1", line), end="")

