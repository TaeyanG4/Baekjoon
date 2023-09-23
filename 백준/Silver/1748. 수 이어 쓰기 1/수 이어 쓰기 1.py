## taeyang's template (1.0.7)
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
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    # n, m = map(int, input().split())
    # lst = [*map(int, input().split())]
    n = int(input())
    nine = '9'
    
    # output
    ans = 0
    while n >= 9 * 10 ** (len(nine)-1):
        ans += 9 * 10 ** (len(nine) - 1) * len(nine)
        n -= 9 * 10 ** (len(nine)-1)
        nine += '9'
    ans += n * len(nine)
    print(ans)
