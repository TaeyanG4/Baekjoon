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


def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    # n, m = map(int, input().split())
    # lst = [*map(int, input().split())]
    n = input().rstrip()
    ans = 0
    for i in range(len(n)-1):
        # 10 ** i : 1 ~ 9, 10 ~ 99, 100 ~ 999, ...
        # (i+1) : 자릿수에 따라 1, 2, 3, ...
        ans += 9 * 10 ** i * (i+1)
    
    # 나머지 처리
    # 만약 n의 자릿수가 3이라면 (10 ** (len(3)-1) - 1)) = 99를 빼고 최종 나머지 자릿수인 len(n)을 곱해준다.
    ans += (int(n) - (10 ** (len(n)-1) - 1)) * len(n) 
    
    # output
    print(ans)