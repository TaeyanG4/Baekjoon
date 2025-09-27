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
    
    while True:
        line = input()
        if not line.strip():
            break
        n, m = map(int, line.split())

        if n == 0 and m == 0:
            break

        calls = []
        for _ in range(n):
            _, _, start, dur = S()
            calls.append((start, start + dur))

        for _ in range(m):
            mon_start, mon_dur = S()
            mon_end = mon_start + mon_dur
            
            ans = 0
            for call_start, call_end in calls:
                if call_start < mon_end and mon_start < call_end:
                    ans += 1
            print(ans)