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


def solution(ax1, ay1, bx2, by2, planet):
    
    ans = 0
    for cx, cy, r in planet:
        if distance(ax1, ay1, cx, cy) < r and not distance(bx2, by2, cx, cy) < r:
            ans += 1
        elif not distance(ax1, ay1, cx, cy) < r and distance(bx2, by2, cx, cy) < r:
            ans += 1
    return ans


def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    t = int(input())
    for _ in range(t):
        planet = []
        ax1, ay1, bx2, by2 = S()
        for _ in range(int(input())):
            cx, cy, r = S()
            planet.append((cx, cy, r))
        print(solution(ax1, ay1, bx2, by2, planet))