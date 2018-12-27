# https://www.hackerrank.com/challenges/html-parser-part-1/problem

def parseHTML(html):
    length = len(html)
    for i in range(length):
      if (html[i] == '<'):
        # new tag found
        l_j = i + 1
        r_j = i
        



        print("Start : html")
        print("End   : title")
        print("-> data-modal-target > None")
        print("End   : h1")
        print("Empty : br")
        print("End   : body")
        print("End   : html")




N = int(input())

for t_itr in range(N):
    html = str(input())
    parsed = parseHTML(html)