"""
Find all substring in a string containing only vowel and having length more than 1
Substring must be contained with two consonants. Print all substrings or -1 if none exists.
"""

import re

v = 'aeiou'
c = 'qwrtypsdfghjklzxcvbnm'

# We use look behind (?<=...) which checks if the condition is met, but doesnt consume it. 
p = re.compile('(?<=[%s])[%s]{2,}[%s]'%(c,v,c), re.I)

m = p.findall(input())

if len(m)>0:
    for i in m:
        print(i[:-1])
else:
    print(-1)
