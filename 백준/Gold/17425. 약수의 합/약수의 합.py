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
    MX = 10**6
    memo = [0] * (MX+1)
    prefix_sum = [0] * (MX+1)
    for i in range(1, MX+1):
        for j in range(1, (MX//i)+1):
            memo[i*j] += i
        prefix_sum[i] = prefix_sum[i-1] + memo[i]
    
    # output
    for _ in range(int(input())):
        print(prefix_sum[int(input())])

    