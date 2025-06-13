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
    
    n, k = S()
    ans_lst = []
    k1, k2 = str(k)[-1], str(k*2)[-1]
    for i in range(1, n+1):
        if str(i)[-1] == k1 or str(i)[-1] == k2:
            continue
        else:
            ans_lst.append(i)
    print(len(ans_lst))
    print(*ans_lst)
    