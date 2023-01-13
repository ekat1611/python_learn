import sys
import re

pattern = r"(\b\w+)\1\b"

for line in sys.stdin:
    if re.search(pattern, line):
        print(line, end = "")



"""
Input:

aaa
aaaa
blabla
go go
go.go
fg blabla
sdfs blabla werw

Output:
aaaa
blabla
fg blabla
sdfs blabla werw
"""