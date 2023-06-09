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
# import statistics as st
# from decimal import *
from collections import *
from itertools import *
# from heapq import *
# from datetime import datetime
#################################


def solution(li):
    for i in range(1, n+1):
        w = li[i][0]
        v = li[i][1]
        for j in range(1, k+1):
            if j < w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
        
    return dp[n][k]

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, k = map(int, input().split())
    li = [[0, 0]]
    for _ in range(n):
        li.append(list(map(int, input().split())))
    dp = [[0] * (k+1) for _ in range(n+1)]

    # output
    print(solution(li))
    
    
    