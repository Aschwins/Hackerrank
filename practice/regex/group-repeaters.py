"""
Find the first repeating alphanumeric character in a string.
If the string contains such a character print that number.
Else print -1.
"""

import re

# Here we use \1+ on a group. A group is indicated by the parenthesis ()
# \1 means that it has to be repeated once.
p = re.compile(r'([a-zA-Z0-9])\1+')

inp = input()
m = p.search(inp)

if m:
    first = m.group(0)[0]
    print(first)
else:
    print(-1)