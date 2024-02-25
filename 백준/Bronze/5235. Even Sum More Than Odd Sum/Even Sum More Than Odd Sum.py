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
# from functools import *
#################################


def solution(lst):
    even, odd = 0, 0
    for i in lst:
        if i % 2:
            odd += i
        else:
            even += i
    
    if even > odd:
        return "EVEN"
    elif even < odd:
        return "ODD"
    else:
        return "TIE"
    
if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    n = int(input())
    for _ in range(n):
        a, *lst = S()
        
        # output
        print(solution(lst))
