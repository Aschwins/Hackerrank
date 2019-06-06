"""
Given N lines substitute input give && with and, and || with or
if and only if it has spaces in front and behind it.
"""
import re

N = int(input())

for i in range(N):
    line = input()
    sub = re.sub("(?<= )(&&)(?= )", "and", line)
    outp = re.sub("(?<= )(\|\|)(?= )", "or", sub)
    print(output)