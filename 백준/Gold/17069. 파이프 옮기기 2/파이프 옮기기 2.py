# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################

def solution():
    # 1행은 1, 열은 0이기 때문에 제외
    for r in range(1, n):
        for c in range(1, n):
            
            # 0: 가로, 1: 대각선, 2: 세로
            # 가로, 세로 파이프 추가
            if mat[r][c] == 0:
                dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1]
                dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c]
            
            # 대각선 파이프 추가
            if mat[r][c] == 0 and mat[r-1][c] == 0 and mat[r][c-1] == 0:
                dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]
    
    return sum(dp[i][n-1][n-1] for i in range(3))
        
if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
    
    # 1행 초기화
    dp[0][0][1] = 1
    for i in range(2, n):
        if mat[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]
        
    # output
    print(solution())
