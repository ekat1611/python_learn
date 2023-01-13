import sys
import re

pattern = r"\b[a]+\b"

for line in sys.stdin:
    fixed = re.sub(pattern, "argh", line, 1, re.IGNORECASE)
    print(fixed, end = "")


"""
Input:

There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA
tata

Output:
There’ll be no more "argh"
argh AaAaAaA
tata
"""