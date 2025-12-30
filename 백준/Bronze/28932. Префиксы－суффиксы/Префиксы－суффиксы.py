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
    for i in range(n):
        for j in range(n):
            for k in range(1, min(len(lst[i]), len(lst[j])) + 1):
                if lst[i][:k] == lst[j][-k:]:
                    return i+1, j+1
    return -1, -1


if __name__ == "__main__":
    # input = sys.stdin.readline
    S = lambda: map(str, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    
    n = int(input())
    lst = [*S()]
    a, b = solution()
    if a == -1:
        print(-1)
    else:
        print(a, b)