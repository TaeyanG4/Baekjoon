## taeyang's template (1.0.4)
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
from itertools import *
# from statistics import *
# from datetime import *
from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

def solution():
    left_li =  li[:n//2]
    right_li = li[n//2:]
    left_sum, right_sum = [], []
    
    for i in range(len(left_li)+1):
        for comb in combinations(left_li, i):
            left_sum.append(sum(comb))
            
    for i in range(len(right_li)+1):
        for comb in combinations(right_li, i):
            right_sum.append(sum(comb))
    
    left_sum.sort()
    ans = 0
    for r in right_sum:
        
        if r > c:
            continue
        
        ans += bisect_right(left_sum, c-r)
        
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, c = map(int, input().split())
    li = [*map(int, input().split())]

    # output
    print(solution())