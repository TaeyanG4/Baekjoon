## taeyang's template (1.0.8)
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
# getcontext().prec = 20
#################################

def solution():
    pass


if __name__ == "__main__":
    # input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    n = int(input())
    cnt = 0
    lst = []
    for i in range(n):
        lst.append(input())
    ans = []
    while True:
        if cnt >= n-1:
            break
        if lst[cnt+1] != 'Present!':
            ans.append(lst[cnt])
            cnt += 1
        else:
            cnt += 2
    if lst[-1] != 'Present!':
        ans.append(lst[-1])
        
    if len(ans) == 0:
        print('No Absences')
    else:
        for i in ans:
            print(i)