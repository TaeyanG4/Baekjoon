# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################

def solution(n):
    ans = INF
    for c in [R, G, B]:
        dp = [[-1]*3 for _ in range(n+1)]
        dp[1] = [INF, INF, INF]
        dp[1][c] = rgb[1][c]
        for i in range(2, n+1):
            dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + rgb[i][R]
            dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + rgb[i][G]
            dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + rgb[i][B]
        dp[n][c] = INF
        ans = min(ans, min(dp[n]))
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n = int(input())
    INF = sys.maxsize
    R, G, B = 0, 1, 2
    rgb = [[-1, -1, -1]]
    for _ in range(n):
        rgb.append(list(map(int, input().split())))
    
    # output
    print(solution(n))