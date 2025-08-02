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
from collections import *
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
    
    a1, a2, a3, b1, b2, b3, L = S()
    if a1*b1 + a2*b2 + a3*b3 < L:
        print(0)
    elif a1*b1 + a2*b2 + a3*b3 == L:
        print(b1 + b2 + b3)
    else:
        tmp = 0
        ans = 0
        dic = {a1: b1, a2: b2, a3: b3}
        
        mx = max(dic.keys())
        for i in range(dic[mx]):
            if tmp >= L:
                break
            tmp += mx
            ans += 1
            
        dic.pop(mx)
        mx = max(dic.keys())
        for i in range(dic[mx]):
            if tmp >= L:
                break
            tmp += mx
            ans += 1
            
        dic.pop(mx)
        mx = max(dic.keys())
        for i in range(dic[mx]):
            if tmp >= L:
                break
            tmp += mx
            ans += 1
            
        dic.pop(mx)
        print(ans)
        
    