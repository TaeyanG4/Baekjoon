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

# https://peisea0830.tistory.com/124

def solution(n):
    dp = [[0] * 14 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(13):
            for k in range(4):
                if i + k <= n:
                    dp[i+k][j+1] += dp[i][j] * math.comb(4, k)
                    
    idx = 1
    ans = 0
    while 4 * idx <= n:
        temp = math.comb(13, idx)
        ans += temp * dp[n - 4 * idx][13 - idx]
        ans %= MOD
        idx += 1
    
    return ans % MOD

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    MOD = 10007
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    
    # output
    print(solution(n))