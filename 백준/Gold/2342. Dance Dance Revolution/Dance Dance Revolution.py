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
from collections import *
# from itertools import *
# from statistics import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def get_dist(cur, target):
    if cur == target:
        return 1
    elif cur == 0:
        return 2
    elif abs(cur - target) % 2 == 0:
        return 4
    else:
        return 3

def solution(cmd):
    # dp[n 번째 움직임][왼발위치][오른발위치]
    dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(len(cmd)+1)]
    dp[0][0][0] = 0
    
    for i in range(1, len(cmd)):
        move = cmd[i-1]
        for left in range(5):
            for right in range(5):
                dp[i][move][right] = min(dp[i][move][right], dp[i-1][left][right] + get_dist(left, move))
                dp[i][left][move] = min(dp[i][left][move], dp[i-1][left][right] + get_dist(right, move))
    
    ans = INF
    for i in range(5):
        for j in range(5):
            ans = min(ans, dp[len(cmd)-1][i][j])
    return ans
    
if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    cmd = deque(map(int, input().split()))
    INF = 1e9

    # output
    print(solution(cmd))