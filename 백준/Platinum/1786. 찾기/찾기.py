# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import time
# import pprint
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

# https://hooongs.tistory.com/305

def getPi(p):
    pi = [0 for _ in range(len(p))]
    
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
            
        if p[i] == p[j]:
            j += 1
            pi[i] = j
            
    return pi
        
def solution(t, pi):
    cnt = 0
    pos = []
    
    j = 0
    for i in range(len(t)):
        while j > 0 and t[i] != p[j]:
            j = pi[j-1]
            
        if t[i] == p[j]:
            if j == len(p)-1:
                cnt += 1
                pos.append(i-len(p)+2)
                j = pi[j]
            else:
                j += 1
    return cnt, pos

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    t = input().rstrip()
    p = input().rstrip()
    
    # output
    cnt, pos = solution(t, getPi(p))
    print(cnt)
    print(*pos)