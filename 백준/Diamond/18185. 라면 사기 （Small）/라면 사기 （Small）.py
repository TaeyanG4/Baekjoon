## taeyang's template (1.0.8)
# https://oh2279.tistory.com/133
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
# from functools import *
#################################


def solution(n, lst):
    
    ans = 0
    for i in range(n):
        
        # 두번째 값이 세번째 값보다 작을 때
        if lst[i+1] < lst[i+2]:
            mi_cnt = min(lst[i], lst[i+1], lst[i+2])
            ans += 7 * mi_cnt
            lst[i] -= mi_cnt
            lst[i+1] -= mi_cnt
            lst[i+2] -= mi_cnt
            
            mi_cnt = min(lst[i], lst[i+1])
            ans += 5 * mi_cnt
            lst[i] -= mi_cnt
            lst[i+1] -= mi_cnt
        
        # 두번째 값이 세번째 값보다 클 때
        else:
            mi_cnt = min(lst[i], lst[i+1]-lst[i+2])
            ans += 5 * mi_cnt
            lst[i] -= mi_cnt
            lst[i+1] -= mi_cnt
            
            mi_cnt = min(lst[i], lst[i+1], lst[i+2])
            ans += 7 * mi_cnt
            lst[i] -= mi_cnt
            lst[i+1] -= mi_cnt
            lst[i+2] -= mi_cnt
        
        ans += 3 * lst[i]
        # lst[i] = 0 # 디버깅용
    
    return ans
        
if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    n = int(input())
    lst = [*map(int, input().split())] + [0, 0]
    
    # output
    print(solution(n, lst))