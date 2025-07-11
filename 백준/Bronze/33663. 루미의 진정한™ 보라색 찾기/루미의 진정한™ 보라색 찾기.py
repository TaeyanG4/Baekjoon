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
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    hlo, hhi = S()
    slo, shi = S()
    vlo, vhi = S()
    R, G, B = S()
    V, m = max(R, G, B), min(R, G, B)
    S = 255*((V-m)/V)
    C = V-m
    if C == 0:
        H = 0
    elif V == R:
        H = 60*((G-B)/(V-m))
        if H < 0:
            H += 360
    elif V == G:
        H = 120 + (60*((B-R)/(V-m)))
        if H < 0:
            H += 360
    elif V == B:
        H = 240 + (60*((R-G)/(V-m)))
        if H < 0:
            H += 360
    if V < vlo or V > vhi:
        print('Lumi will not like it.')
    elif S < slo or S > shi:
        print('Lumi will not like it.')
    else:
        if hlo <= H <= hhi:
            print('Lumi will like it.')
        else:
            print('Lumi will not like it.')