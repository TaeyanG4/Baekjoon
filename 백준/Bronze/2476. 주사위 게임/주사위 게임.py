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

def solution():
    ans = 0
    for _ in range(t):
        a, b, c = map(int, input().split())
        if a == b == c:
            ans = max(ans, 10000 + a * 1000)
        elif a == b:
            ans = max(ans, 1000 + a * 100)
        elif b == c:
            ans = max(ans, 1000 + b * 100)
        elif c == a:
            ans = max(ans, 1000 + c * 100)
        else:
            ans = max(ans, max(a, b, c) * 100)
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    # n, m = map(int, input().split())
    # li = [*map(int, input().split())]
    t = int(input())
    
    # output
    print(solution())