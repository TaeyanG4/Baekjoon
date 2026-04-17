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
    S = lambda: map(float, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    s, t = input().rstrip(), input().rstrip()
    s_cnt = [0]*26
    t_cnt = [0]*26
    for c in s[1:]:
        s_cnt[ord(c)-ord('a')] += 1
    for c in t[:-1]:
        t_cnt[ord(c)-ord('a')] += 1
    ans = len(s) * len(t)
    for i in range(26):
        ans -= s_cnt[i] * t_cnt[i]
    print(ans)