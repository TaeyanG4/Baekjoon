## taeyang's template (1.0.7)
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
import pprint
# from collections import *
# from heapq import *
# from queue import PriorityQueue
from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################


def solution():
    ans = INF
    row, col = [sum(i) for i in board], [sum(i) for i in zip(*board)]
    new_board = [i+j for i, j in zip(row, col)]
    total_sum = sum(new_board) // 2

    for combi in combinations(new_board, n//2):
        ans = min(ans, abs(total_sum-sum(combi)))
        if ans == 0:
            return ans
    
    for combi in combinations(new_board, n//2 + 1):
        ans = min(ans, abs(total_sum-sum(combi)))
        if ans == 0:
            return ans
    
    return ans


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    n = int(input())
    board = [[*map(int, input().split())] for _ in range(n)]
    
    # output
    print(solution())