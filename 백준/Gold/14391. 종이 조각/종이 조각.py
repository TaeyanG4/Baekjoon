## taeyang's template (1.0.8)
# https://lagooni.tistory.com/entry/백준-종이-조각-14391번-Python-Bitmasking
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


def solution():
    
    # bitmastking
    ans = 0
    for i in range(1 << (n*m)):
        total = 0
        
        # horizontal sum
        for r in range(n):
            rsum = 0
            for c in range(m):
                idx = r*m + c
                if not i & (1 << idx):
                    rsum = rsum * 10 + board[r][c]
                else:
                    total += rsum
                    rsum = 0
            total += rsum
            
        # vertical sum
        for c in range(m):
            csum = 0
            for r in range(n):
                idx = r*m + c
                if i & (1 << idx):
                    csum = csum * 10 + board[r][c]
                else:
                    total += csum
                    csum = 0
            total += csum
        ans = max(ans, total)
    return ans


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    # n = int(input())
    n, m = map(int, input().split())
    board = [[*map(int, input().rstrip())] for _ in range(n)]
    
    # output
    print(solution())