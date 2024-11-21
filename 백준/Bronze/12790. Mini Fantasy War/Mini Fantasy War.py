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

    for _ in range(int(input())):
        hp, mp, atk, dfs, h, m, a, d = S()
        hp += h
        mp += m
        atk += a
        dfs += d
        if hp <= 1:
            hp = 1
        if mp <= 1:
            mp = 1
        if atk <= 0:
            atk = 0
        print(1*hp + 5*mp + 2*atk + 2*dfs)