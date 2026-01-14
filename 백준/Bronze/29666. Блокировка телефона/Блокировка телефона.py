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
    
    
    s = input().rstrip()
    s = s.replace(' ', '')
    a, b, c = map(int, s)
    pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        0:(3,1)
    }
    cc = [pos[a], pos[b], pos[c]]
    rs = [r for r, _ in cc]
    cs = [ca for _, ca in cc]
    if len({a, b, c}) != 3:
        print("Locked")
    elif len(set(rs)) == 1:
        sc = sorted(cs)
        if sc[1] == sc[0] + 1 and sc[2] == sc[1] + 1:
            print("Unlocked")
        else:
            print("Locked")
    elif len(set(cs)) == 1:
        sr = sorted(rs)
        if sr[1] == sr[0] + 1 and sr[2] == sr[1] + 1:
            print("Unlocked")
        else:
            print("Locked")
    else:
        print("Locked")