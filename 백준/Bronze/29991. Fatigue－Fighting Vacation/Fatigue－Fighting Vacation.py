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

    d, c, r = S()
    c_lst = []
    ans = 0
    
    for _ in range(c):
        c_lst.append(int(input()))
    
    for _ in range(r):
        d += int(input())
        ans += 1
    
    for i in c_lst:
        if d < i:
            break
        d -= i
        ans += 1
    
    print(ans)
    