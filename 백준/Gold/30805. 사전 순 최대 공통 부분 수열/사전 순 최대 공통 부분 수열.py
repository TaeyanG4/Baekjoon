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


def solution(n, lst_a, m, lst_b):
    
    sorted_lst_a = sorted(lst_a, reverse=True)
    ans = []
    for i in sorted_lst_a:
        if i in lst_a and i in lst_b:
            ans.append(i)
            lst_a = lst_a[lst_a.index(i)+1:]
            lst_b = lst_b[lst_b.index(i)+1:]
    
    return len(ans), ans
        

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    n = int(input())
    lst_a = [*map(int, input().split())]
    m = int(input())
    lst_b = [*map(int, input().split())]
    
    # output
    k, ans = solution(n, lst_a, m, lst_b)
    print(k)
    print(*ans)