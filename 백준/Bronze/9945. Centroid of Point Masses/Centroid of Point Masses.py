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

    cnt = 1
    while True:
        n = int(input())
        if n < 0:
            break
        X, Y, M = 0, 0, 0
        for _ in range(n):
            x, y, m = S()
            X += x * m
            Y += y * m
            M += m
        print(f'Case {cnt}: {X/M:.2f} {Y/M:.2f}')
        tmp = input()
        cnt += 1