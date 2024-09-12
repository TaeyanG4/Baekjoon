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
from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
# from functools import *
#################################


def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    lst = []
    n = int(input())
    for _ in range(n):
        lst.append([*map(int, input().split())])
    
    for i in range(3):
        dic = defaultdict(int)
        for j in range(n):
            dic[lst[j][i]] += 1
        
        se = set()
        for k, v in dic.items():
            if v >= 2:
                se.add(k)
        
        for j in range(n):
            if lst[j][i] in se:
                lst[j][i] = 0
        
    for line in lst:
        print(sum(line))