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
    sol = [
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
        (1, 1, 1),
        None,
        None,
        (-1, -1, 2),
        (0, -1, 2),
        (0, 0, 2),
        (0, 1, 2),
        (1, 1, 2),
        (-2, -2, 3),
        (7, 10, -11),
        None,
        None,
        (-1, 2, 2),
        (-511, -1609, 1626),
        (1, 2, 2),
        (-1, -2, 3),
        (0, -2, 3),
        (1, -2, 3),
        (-11, -14, 16),
        None,
        None,
        (-2901096694, -15550555555, 15584139827),
        (-1, -1, 3),
        (0, -1, 3),
        (0, 0, 3),
        (0, 1, 3),
        (1, 1, 3),
        (-283059965, -2218888517, 2220422932),
        None,
        None,
        (8866128975287528, -8778405442862239, -2736111468807040),
        (-1, 2, 3),
        (0, 2, 3),
        (1, 2, 3),
        (0, -3, 4),
        (1, -3, 4),
        (117367, 134476, -159380),
        None,
        None,
        (-80538738812075974, 80435758145817515, 12602123297335631),
        (2, 2, 3),
        (-5, -7, 8),
        (2, -3, 4),
        (-2, 3, 3),
        (6, 7, -8),
        (-23, -26, 31),
        None,
    ]
    if sol[n] is None:
        print(0)
    else:
        print(*sol[n])