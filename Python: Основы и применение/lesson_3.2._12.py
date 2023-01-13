import sys
import re

pattern = r"human"

for line in sys.stdin:
    new_str = re.sub(pattern, "computer", line)
    print(new_str, end = "")


"""
Input:
I need to understand the human mind
humanity

Output:
I need to understand the computer mind
computerity
"""