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

def solution(mm, dd):
    pass

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    
    sh1, sm1, eh1, em1 = S()
    sh2, sm2, eh2, em2 = S()
    sh3, sm3, eh3, em3 = S()
    
    s_tmp1, e_tmp1 = sh1*60 + sm1, eh1*60 + em1
    s_tmp2, e_tmp2 = sh2*60 + sm2, eh2*60 + em2
    s_tmp3, e_tmp3 = sh3*60 + sm3, eh3*60 + em3
    
    if s_tmp1 > e_tmp1: e_tmp1 += 24*60
    if s_tmp2 > e_tmp2: e_tmp2 += 24*60
    if s_tmp3 > e_tmp3: e_tmp3 += 24*60
    
    tmp1, tmp2, tmp3 = e_tmp1-s_tmp1, e_tmp2-s_tmp2, e_tmp3-s_tmp3
    mx_tmp, mi_tmp = max(tmp1, tmp2, tmp3), min(tmp1, tmp2, tmp3)
    
    print(f'{mi_tmp//60}:{mi_tmp%60:02}')
    print(f'{mx_tmp//60}:{mx_tmp%60:02}')
