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

    # input
    n = int(input())
    se = set()
    lst = []
    
    for _ in range(n):
        v = int(input())
        se.add(v)
        lst.append(v)
    
    ans = 0
    for i in list(se):
        new_lst = [x for x in lst if x != i]
        d = -1
        cnt = 0
        for j in new_lst:
            if d == -1:
                d = j
                cnt += 1
            else:
                if d == j:
                    cnt += 1
                else:
                    d = j
                    cnt = 1
            ans = max(ans, cnt)
    print(ans)