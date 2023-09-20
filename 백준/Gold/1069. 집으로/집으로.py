## taeyang's template (1.0.7)
# https://ca.ramel.be/142
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


def dist(p1, p2):
    return ((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2) ** 0.5


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
    x, y, d, t = [*map(int, input().split())]
    xyd = dist((0, 0), (x, y))
    
    # 전체거리가 d보다 크거나 같은 경우
    if xyd >= d:
        case1 = ((xyd//d) * t) + xyd % d # 점프하고 남은 거리를 걸어가는 경우
        case2 = (xyd//d + 1) * t # 점프하고 도착 직전에 꺽어서 점프하는 경우
        case3 = xyd # 점프하지 않고 걸어가는 경우
    
    # 전체거리가 d보다 작은 경우
    else:
        case1 = d-xyd+t # 점프하고 남은 거리를 걸어가는 경우 (꺽는 경우가 있기 때문에 2번이상 점프하지 않는다.)
        case2 = 2*t # 2번 점프하는 경우 (꺽는 경우)
        case3 = xyd # 점프하지 않고 걸어가는 경우

    # output
    print(min(case1, case2, case3))
