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
# import pprint
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(s, n):
    dp = [[False] * (n+1) for _ in range(n+1)]
    res = [INF] * (n+1)
    res[0] = 0
    
    # 길이가 1인경우 무조건 펠린드롬
    for i in range(1, n+1):
        dp[i][i] = True
    
    # 길이가 2인경우 이전과 비교하여 펠린드롬인지 확인
    for i in range(1, n):
        if s[i-1] == s[i]:
            dp[i][i+1] = True
    
    # 길이가 3이상인경우 이전과 비교하여 펠린드롬인지 확인
    # size는 크기, i는 시작점, dp[i+1][size+i-1]은 이전의 펠린드롬인지 확인
    for size in range(2, n):
        for i in range(1, n+1-size):
            if s[i-1] == s[i+size-1] and dp[i+1][size+i-1]:
                dp[i][size+i] = True
    
    # i를 진행하면서 그 뒤쪽의 res값에 대해 j가 계속 최신화를 시켜주며 최솟값으로 갱신
    for i in range(1, n+1):
        # res[i-1] + 1인 이유는 i-1까지의 최솟값에 j부터 i까지의 펠린드롬하나를 더해줌
        res[i] = min(res[i], res[i-1] + 1)
        for j in range(i+1, n+1):
            if dp[i][j]:
                res[j] = min(res[j], res[i-1] + 1)
    
    return res[n]

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    s = input().rstrip()
    n = len(s)
    
    # output
    print(solution(s, n))