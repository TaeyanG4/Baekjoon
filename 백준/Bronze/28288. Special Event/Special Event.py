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
    board = [list(input().rstrip()) for _ in range(n)]
    ans = []
    mx = 0
    for i, line in enumerate(zip(*board)):
        cnt_y = line.count('Y')
        if cnt_y > mx:
            mx = cnt_y
            ans = [i+1]
        elif cnt_y == mx:
            ans.append(i+1)
    print(','.join(map(str, ans)))