## taeyang's template (1.0.7)
# https://hazung.tistory.com/127
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
from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

# 일치하는지 확인
def checker(idx):
    sm = 0
    for i in range(idx, -1, -1):
        sm += ans[i]
        if board[i][idx] != 0 and sm == 0:
            return False
        elif board[i][idx] <= 0 and sm > 0:
            return False
        elif board[i][idx] >= 0 and sm < 0:
            return False
    return True


def dfs(idx):
    if idx == n:
        return True
    
    # 0일 경우
    if board[idx][idx] == 0:
        ans[idx] = 0
        return dfs(idx + 1)
    
    # 0이 아닐 경우
    for i in range(1, 11):
        ans[idx] = board[idx][idx] * i
        if checker(idx) and dfs(idx + 1):
            return True
        
    # 값이 없을 경우
    return False


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    n = int(input())
    s = deque(input().rstrip())
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            x = s.popleft()
            if x == '+':
                board[i][j] = 1
            elif x == '-':
                board[i][j] = -1
    
    # dfs
    ans = [0] * n
    dfs(0)
        
    # output
    print(*ans)