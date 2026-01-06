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
    s = input().rstrip()
    a = int(input())
    if s[0] == 'i':
        if a % 2 == 0:
            print(a)
        else:
            if a+1 > n:
                print(a-1)
            else:
                print(a+1)
    else:
        if a % 2 == 1:
            print(a)
        else:
            if a+1 > n:
                print(a-1)
            else:
                print(a+1)
    