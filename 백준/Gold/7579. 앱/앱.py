# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

# https://claude-u.tistory.com/445

def solution(n, m, app_li, cost_li):
    res = sum(cost_li)
    
    for i in range(1, n+1):
        byte = app_li[i]
        cost = cost_li[i]
        
        for j in range(1, sum(cost_li) + 1):
            if j-1 < cost:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + byte)
            
            if dp[i][j] >= m:
                res = min(res, j-1)
    if m != 0:
        return res
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n, m = map(int, input().split())
    app_li = [0] + list(map(int, input().split()))
    cost_li = [0] + list(map(int, input().split()))
    dp = [[0 for _ in range(sum(cost_li)+1)] for _ in range(n+1)]
    
    # output
    print(solution(n, m, app_li, cost_li))