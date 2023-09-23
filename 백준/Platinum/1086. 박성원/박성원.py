## taeyang's template (1.0.7)
# https://suuntree.tistory.com/124
# https://nicotina04.tistory.com/73
# https://velog.io/@jini_eun/백준-1086번-박성원-Java-Python
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
    """
        나눗셈의 나머지 연산:
            (a+b)%m=(a%m+b%m)%m

        d[i | (1 << i)][next] += dp[i][j]
        next = (새로만들어진 수) % k
            = (원래 수 * pow( 10, len(l번째 수) ) + l번째 수) % k 
            = [(원래 수 * pow( 10, len(l번째 수) ) ) % k  + l번째 수 % k] % k
            = [(원래 수 % k  * pow( 10, len(l번째 수)) % k ) % k + l번째 수 % k] % k
            = [(j * pow(10, len(l번째 수)) % k) % k + l번째 수 % k] % k
        
        원래수 % k = j
        l번째 수 % k = lst[i]
        
        r[i][j] = (j * pow(10, len(lst[i])) % k) % k + lst[i] % k
    """
    
    r = [[(j * pow(10, len(str(lst[i]))) % k + lst[i] % k) % k for j in range(k)] for i in range(n)]
    memo = [[0] * k for _ in range(1 << n)]
    memo[0][0] = 1
        
    for bm in range(1 << n):
        for i in range(n):
            if bm & (1 << i):
                continue
            for j in range(k):
                memo[bm | (1 << i)][r[i][j]] += memo[bm][j]
                
    p = memo[(1 << n) - 1][0]
    q = sum(memo[(1 << n) - 1])
    g = math.gcd(p, q)
    return f"{p // g}/{q // g}"


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
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    k = int(input())
    
    # output
    print(solution())
