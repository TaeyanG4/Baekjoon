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


def solution(s):
    s = s[::-1]
    lst = s.split()
    lst = lst[::-1]
    return lst


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    t = int(input())

    for _ in range(t):
        # input
        s = input().rstrip()
        
        # output
        print(*solution(s))
