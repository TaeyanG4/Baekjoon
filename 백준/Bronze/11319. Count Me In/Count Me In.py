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
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    lst = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for _ in range(int(input())):
        con, vol = 0, 0
        for c in input().rstrip():
            if c in ' ':
                continue
            elif c in lst:
                vol += 1
            else:
                con += 1
        print(con, vol)