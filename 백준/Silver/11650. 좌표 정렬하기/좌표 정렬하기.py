import sys
input = sys.stdin.readline
import math
from collections import *
from itertools import *

def sol(l):
    l.sort(key=lambda x: (x[0],x[1]))
    return l

if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l = sol(l)
    for x,y in l:
        print(x, y)