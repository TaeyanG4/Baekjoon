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

def find(vroot, n):
    while vroot[n] != n:
        n = vroot[n]
    return n

def solution(n):
    elist = []
    ans = 0
    
    xlst,ylst,zlst = [],[],[]
    for i in range(n):
        x, y, z = map(int,input().split())
        xlst.append((x, i))
        ylst.append((y, i))
        zlst.append((z, i))
    xlst.sort(); ylst.sort(); zlst.sort()
    
    for cur in [xlst, ylst, zlst]:
        for i in range(1, n):
            w1, a = cur[i-1]
            w2, b = cur[i]
            elist.append((abs(w1-w2), a, b))
    elist.sort()
    
    for w, s, e in elist:
        sroot = find(vroot, s)
        eroot = find(vroot, e)
        if sroot != eroot:
            if sroot > eroot:
                vroot[sroot] = eroot
            else:
                vroot[eroot] = sroot
            ans += w
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n = int(input())
    vroot = [i for i in range(n)]
    
    # output
    print(solution(n))
