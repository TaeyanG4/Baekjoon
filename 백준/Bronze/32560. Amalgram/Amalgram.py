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
    
    alpha_cnt1, alpha_cnt2 = [0] * 26, [0] * 26
    s1, s2 = input().strip(), input().strip()
    for i in s1:
        alpha_cnt1[ord(i) - ord('a')] += 1
    for i in s2:
        alpha_cnt2[ord(i) - ord('a')] += 1
    for i in range(26):
        mx = max(alpha_cnt1[i], alpha_cnt2[i])
        print(chr(ord('a')+i)*mx, end='')