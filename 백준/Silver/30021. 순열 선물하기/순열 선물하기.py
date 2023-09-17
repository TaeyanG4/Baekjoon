## taeyang's template (1.0.5)
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
#################################

def solution(n):
    if n == 1:
        return 'YES', [1]
    elif n == 2:
        return 'NO', []
    elif n == 3:
        return 'YES', [1, 3, 2]
    elif n >= 4:
        seq = [1, 3 ,2]
        seq.extend([i for i in range(4, n+1)])
        return 'YES', seq
    
if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    # n, m = map(int, input().split())
    # lst = [*map(int, input().split())]
    n = int(input())
    
    # output
    y_n, ans = solution(n)
    print(y_n)
    if y_n == 'YES':
        print(*ans)