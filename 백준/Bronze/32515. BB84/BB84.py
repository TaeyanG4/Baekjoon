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
    
    n = int(input())
    vh_z = input().strip()
    zo_z = input().strip()
    vh_y = input().strip()
    zo_y = input().strip()
    
    ans = ''
    for i in range(n):
        if vh_z[i] == vh_y[i]:
            if zo_z[i] != zo_y[i]:
                print("htg!")
                break
            else:
               ans += zo_z[i]
    else:
        print(ans)
