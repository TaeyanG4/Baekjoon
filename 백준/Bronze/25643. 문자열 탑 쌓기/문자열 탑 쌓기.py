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
from itertools import *
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

    n, m = S()
    lst = []
    for _ in range(n):
        lst.append(input().strip())
    
    for i in range(n-1):
        s1, s2 = lst[i], lst[i+1]
        flag = False
        for j in range(1, m+1):
            if s1[m-j:] == s2[:j]:
                flag = True
                break
            if s1[:j] == s2[m-j:]:
                flag = True
                break
        if not flag:
            print(0)
            break
    else:
        print(1)