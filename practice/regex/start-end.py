"""
Given string S, give start and end locations of substring s in tuples
seperated by \n
"""
import re

S = input()
s = input()

p = re.compile(r'({0})'.format(s))

m = p.search(S)

if m:
    start = 0
    while m:
        print(tuple([m.start(), m.end() - 1]))
        start = m.start() + 1
        m = p.search(S, start)
else:
    print(tuple([-1, -1]))