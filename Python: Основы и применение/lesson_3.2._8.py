import sys
import re


# метасимвол \b позволяет вытащить слово целиком
pattern = r"\bcat\b"

for line in sys.stdin:
    if re.findall(pattern, line):
        print(line)


"""
Input:

cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?


Output:

cat
catapult and cat
"cat"
!cat?
"""