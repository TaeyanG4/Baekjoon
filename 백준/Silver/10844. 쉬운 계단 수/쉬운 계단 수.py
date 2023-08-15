## taeyang's template (1.0.0)
#################################
## my import lines
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

def solution(n):
    
    dp = [[0] * 10 for _ in range(n+1)]
    
    for i in range(1, 10):
        dp[1][i] = 1
    
    for i in range(2, n+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    
    return sum(dp[n]) % MOD

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    MOD = 1000000000
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    
    # output
    print(solution(n))