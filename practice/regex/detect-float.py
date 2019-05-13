# Checks if input is a valid floating point number.
# https://www.hackerrank.com/challenges/introduction-to-regex/problem

# Sample input:
# Number of input lines N followed by input with sep \n

"""
4
4.0O0
-1.00
+4.54
SomeRandomStuff
"""

import re

p = re.compile(r'[\+\-]?[0-9]*\.[0-9]+')

N = int(input())

for i in range(N):
    inp = input()
    m = p.match(inp)
    if m:
        print(m.end() == len(inp))
    else:
        print(False)