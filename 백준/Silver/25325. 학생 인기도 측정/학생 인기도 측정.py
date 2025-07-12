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
    input = sys.stdin.readline
    S = lambda: map(str, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    n = int(input())
    name_lst = S()
    dic = {name: 0 for name in name_lst}
    for _ in range(n):
        lst = S()
        for name in lst:
            dic[name] += 1
    ans = []
    for name, cnt in dic.items():
        ans.append((name, cnt))
    ans.sort(key=lambda x: x[1], reverse=True)
    for name, cnt in ans:
        print(name, cnt)