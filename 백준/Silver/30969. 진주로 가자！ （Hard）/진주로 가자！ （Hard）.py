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
    S = lambda: map(str, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    n = int(input())
    jinju = None
    diff = [0] * 1002
    over_1000 = 0
    for i in range(n):
        name, pay = S()
        if name == 'jinju':
            jinju = int(pay)
        elif int(pay) > 1000:
            over_1000 += 1
        else:
            diff[int(pay)] += 1
    print(jinju)
    print(sum(diff[jinju+1:]) + over_1000)