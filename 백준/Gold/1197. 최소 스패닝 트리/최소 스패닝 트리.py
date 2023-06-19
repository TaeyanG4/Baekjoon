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
# https://johoonday.tistory.com/152
# https://hillier.tistory.com/54

def find(x):
        global vroot
        if x != vroot[x]:
            vroot[x] = find(vroot[x])
        return vroot[x]

def solution1(v, e, vroot, elist):
    
    # kruskal algorithm
    ans = 0
    elist.sort(key=lambda x: x[2]) # 가중치 기준으로 오름차순 정렬
    for s, e, w in elist:
        sroot = find(s)
        eroot = find(e)
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
    v, e = map(int, input().split())
    vroot = [i for i in range(v+1)]
    elist = [] 
    for _ in range(e):
        elist.append(list(map(int, input().split())))
    
    # output
    print(solution1(v, e, vroot, elist))
    
# 3 3
# 1 2 1
# 2 3 2
# 1 3 3