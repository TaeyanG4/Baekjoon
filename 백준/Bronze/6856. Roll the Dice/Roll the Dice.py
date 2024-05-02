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

    cnt = 0
    n, m = int(input()), int(input())
    if n > m:
        n, m = m, n
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i+j == 10:
                cnt += 1
    if cnt == 1:
        print(f'There is {cnt} way to get the sum 10.')
    else:
        print(f'There are {cnt} ways to get the sum 10.')