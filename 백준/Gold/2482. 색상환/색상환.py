## taeyang's template (1.0.7)
# https://ca.ramel.be/149
# https://velog.io/@yoopark/baekjoon-2482
# https://velog.io/@jini_eun/백준-2482번-색상환-Java-Python
# https://hooongs.tistory.com/320
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
    if n // 2 < k:
        return 0
    else:
        # memo[i][j] = 1~i번째 색만 가지고 인접하지 않도록 j개의 색을 선택하는 경우의 수
        memo = [[0] * (k + 1) for _ in range(n + 1)]
        
        # 초기화
        for i in range(n + 1):
            memo[i][0] = 1
            memo[i][1] = i
        
        # 선형일때 경우의 수
        for i in range(2, n + 1):
            for j in range(2, k + 1):
                memo[i][j] = (memo[i - 1][j] + memo[i - 2][j - 1]) % MOD

        # 원형일때 경우의 수
        return (memo[n - 1][k] + memo[n - 3][k - 1]) % MOD


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    INF = float('inf')
    MOD = 10**9 + 3
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    n = int(input())
    k = int(input())
    

    # output
    print(solution())
