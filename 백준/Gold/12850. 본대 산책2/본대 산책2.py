# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import time
import pprint
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

# https://kangminjun.tistory.com/entry/BOJ-12850번-본대-산책2
# https://velog.io/@sunkyuj/python-백준-12850-본대-산책2

def solution(n, s, e):
    if n <= 1:
        return memo[n][s][e]
    
    memo.setdefault(n, [[0 for _ in range(8)] for _ in range(8)])
    if memo[n][s][e]:
        return memo[n][s][e]
    
    half = n // 2
    other = half + 1 if n % 2 else half # 홀수면 +1
    
    for i in range(8):
        memo[n][s][e] += solution(half, s, i) * solution(other, i, e)
        memo[n][s][e] %= 1000000007
    
    return memo[n][s][e]

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    memo = {}
    memo[1] = [
        [0, 1, 1, 0, 0, 0, 0, 0], # 정보과학관
        [1, 0, 1, 1, 0, 0, 0, 0], # 전산관
        [1, 1, 0, 1, 1, 0, 0, 0], # 미래관
        [0, 1, 1, 0, 1, 1, 0, 0], # 신양관
        [0, 0, 1, 1, 0, 1, 0, 1], # 한경직기념관
        [0, 0, 0, 1, 1, 0, 1, 0], # 진리관
        [0, 0, 0, 0, 0, 1, 0, 1], # 학생회관
        [0, 0, 0, 0, 1, 0, 1, 0]  # 형남공학관
    ]
    
    # output
    print(solution(n, 0, 0))