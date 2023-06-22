# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################

def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def find(vroot, n):
    while vroot[n] != n:
        n = vroot[n]
    return n

def solution(n, p):
    elist = []
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            w = dist(p[i], p[j])
            heappush(elist, (w, i, j))
    
    for _ in range(len(elist)):
        w, s, e = heappop(elist)
        sroot = find(vroot, s)
        eroot = find(vroot, e)
        if sroot != eroot:
            if sroot > eroot:
                vroot[sroot] = eroot
            else:
                vroot[eroot] = sroot
            ans += w
    return round(ans, 2)

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n = int(input())
    p = []
    vroot = [i for i in range(n)]
    for _ in range(n):
        p.append(list(map(float, input().split())))
    
    # output
    print(solution(n, p))
