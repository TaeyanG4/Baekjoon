## taeyang's template (1.0.1)
# https://post.naver.com/viewer/postView.nhn?volumeNo=28894924&memberNo=33264526&vType=VERTICAL
# https://suri78.tistory.com/15
#################################
## my import lines
import sys
# import math
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
# from datetime import *
# from bisect import *
#################################

# def solution(k, li):
    
#     dp = [[0] * (k+1) for _ in range(k+1)]
#     prefix_sum = [0] * (k+1)
#     for i in range(k):
#         prefix_sum[i] = prefix_sum[i-1] + li[i]
    
#     for g in range(1, k):
#         for s in range(k-g):
#             e = s + g
#             dp[s][e] = INF
#             for i in range(s, e):
#                 dp[s][e] = min(dp[s][e], dp[s][i] + dp[i+1][e] + prefix_sum[e] - prefix_sum[s-1])
#     # print(prefix_sum)
#     # pprint.pprint(dp)
#     return dp[0][k-1]

def solution(k, li):
    
    # dp + prefix_sum
    dp = [[0] * (k) for _ in range(k)]
    for i in range(k-1):
        dp[i][i+1] = li[i] + li[i+1]
        for j in range(i+2, k):
            dp[i][j] = dp[i][j-1] + li[j]
            
    for g in range(2, k):
        for s in range(k-g):
            e = s + g
            min_vals = []
            for i in range(s, e):
                min_vals.append(dp[s][i] + dp[i+1][e])
            dp[s][e] += min(min_vals)

    # pprint.pprint(dp)
    return dp[0][k-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    t = int(input())
    
    # output
    for i in range(t):
        k = int(input())
        li = list(map(int, input().split()))
        print(solution(k, li))