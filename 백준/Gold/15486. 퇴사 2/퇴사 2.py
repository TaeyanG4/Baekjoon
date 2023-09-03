## taeyang's template (1.0.4)
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
#################################

def solution(n, li):
    memo = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        day, pay = li[i]
        if day+i > n:
            memo[i] = memo[i+1]
        else:
            memo[i] = max(memo[i+1], pay+memo[i+day])
    
    return memo[0]

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    li = [[*map(int, input().split())] for _ in range(n)]
    
    # output
    print(solution(n, li))