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

    n = int(input())
    lst = []
    for _ in range(n):
        a, t = S()
        lst.append([a, t])
    lst.sort(key=lambda x: x[0])
    for i in range(n-1):
        a1, t1 = lst[i]
        a2, t2 = lst[i+1]
        if a1+t1 > a2:
            lst[i+1][0] = a1+t1
    print(lst[-1][0]+lst[-1][1])