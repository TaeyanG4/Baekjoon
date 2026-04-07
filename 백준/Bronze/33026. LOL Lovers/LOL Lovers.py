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
    s = input().rstrip()
    for i in range(n-1):
        m, f = s[:i+1], s[i+1:]
        m_l, m_o, f_l, f_o = m.count('L'), m.count('O'), f.count('L'), f.count('O')
        if m_l != f_l and m_o != f_o:
            print(i+1)
            break
    else:
        print(-1)