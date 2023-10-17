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

def backtracking_mx(depth):
    global mx
    if depth == n + 1:
        return True
    for i in range(9, -1, -1):
        if not visited_mx[i]:
            if depth == 0 or (lst[depth - 1] == '<' and mx[-1] < i) or (lst[depth - 1] == '>' and mx[-1] > i):
                visited_mx[i] = True
                mx.append(i)
                if backtracking_mx(depth + 1):
                    return True
                visited_mx[i] = False
                mx.pop()
    return False


def backtracking_mi(depth):
    global mi
    if depth == n + 1:
        return True
    for i in range(10):
        if not visited_mi[i]:
            if depth == 0 or (lst[depth - 1] == '<' and mi[-1] < i) or (lst[depth - 1] == '>' and mi[-1] > i):
                visited_mi[i] = True
                mi.append(i)
                if backtracking_mi(depth + 1):
                    return True
                visited_mi[i] = False
                mi.pop()
    return False


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    n = int(input())
    lst = [*map(str, input().split())]
    mx, mi = [], []
    
    # backtracking mx
    visited_mx = [False] * 10
    backtracking_mx(0)
    visited_mi = [False] * 10
    backtracking_mi(0)
    
    # output
    print(''.join(map(str, mx)))
    print(''.join(map(str, mi)))