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


def solution(n, lst):
    
    s, e = 0, 0
    k = [0] * 10
    k_cnt = 0
    ans = 0
    while True:
        if e == n:
            return ans
        elif k_cnt <= 2:
            k[lst[e]] += 1
            if k[lst[e]] == 1:
                k_cnt += 1
            e += 1
        else:
            k[lst[s]] -= 1
            if k[lst[s]] == 0:
                k_cnt -= 1
            s += 1

        if k_cnt <= 2:
            ans = max(ans, e - s)

                    
if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    n = int(input())
    lst = [*map(int, input().split())]
    
    # output
    print(solution(n, lst))