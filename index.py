import itertools
import math
import sys

n = [line.rstrip('\n') for line in open("sample.in")]

res = []
for i in range(0, len(n)):
    # check unique
    if len(n[i]) == len(set(n[i])):  # all characters are unique
        res.append(math.factorial(len(n[i])))
    else:  # Not unique
        payda = len(n[i]) - len(set(n[i]))
        res.append(int((math.factorial(len(n[i]))) // (2**payda)))

f = open('sample.out', 'w')
for i in range(0,len(res)):
    f.write(str(res[i])+'\n')
f.close()
