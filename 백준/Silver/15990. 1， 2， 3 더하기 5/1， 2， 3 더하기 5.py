## taeyang's template (1.0.8)
# https://sodehdt-ldkt.tistory.com/136
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
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    MOD = 10**9 + 9
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    t = int(input())
    memo = [[0 for _ in range(3)] for _ in range(10**6 + 1)]
    
    # dp
    memo[1] = [1, 0, 0] # 1
    memo[2] = [0, 1, 0] # 2
    memo[3] = [1, 1, 1] # 12, 21, 3
    
    for i in range(4, 10**6 + 1):
        memo[i][0] = (memo[i-1][1] + memo[i-1][2]) % MOD # 마지막 자리가 1이므로 -1한뒤 2, 3으로 끝나는 경우의 수를 더해줌
        memo[i][1] = (memo[i-2][2] + memo[i-2][0]) % MOD # 마지막 자리가 2이므로 -2한뒤 1, 3으로 끝나는 경우의 수를 더해줌
        memo[i][2] = (memo[i-3][0] + memo[i-3][1]) % MOD # 마지막 자리가 3이므로 -3한뒤 1, 2으로 끝나는 경우의 수를 더해줌
    
    # output
    for i in range(t):
        n = int(input())
        print(sum(memo[n]) % MOD)