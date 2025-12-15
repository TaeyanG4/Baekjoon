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
    x = [*S()]
    l = [*S()]
    c = [*map(str, input().split())]
    for i in range(n-1):
        for j in range(i+1, n):
            if (abs(x[i]-x[j]) <= l[i]+l[j]) and (c[i] != c[j]):
                print("YES")
                print(i+1, j+1)
                break
        else:
            continue
        break
    else:
        print("NO")
    