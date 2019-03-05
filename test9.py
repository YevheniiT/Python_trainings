from random import randrange
import re

def brackets (n):
    i, result, brackets = 0, '', '[]'
    while i < n*2:
        result += brackets[randrange(len(brackets))]
        i+=1

    brackets_st = result

    while len (re.findall(r'\[\]', result)) > 0:
        result = re.sub(r'\[\]', '', result)

    if len(result) > 0:
        print(brackets_st, "Not OK")
    else:
        print(brackets_st, "OK")

brackets(7)