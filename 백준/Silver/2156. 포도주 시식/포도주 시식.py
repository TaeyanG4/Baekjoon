## taeyang's template (1.0.0)
# https://velog.io/@bye9/백준파이썬-2156-포도주-시식
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
import pprint
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n, li):
    dp = []
    if n == 1:
        return li[0]
    elif n == 2:
        return li[0] + li[1]
    elif n == 3:
        return max(li[0] + li[1], li[0] + li[2], li[1] + li[2])
    else:
        
        # i번째 포도주를 마시고 i-2번째까지 마신 양, 
        # i,i-1번째를 포도주를 마시고 i-3번째까지 마신 양, 
        # i번째를 마시지 않는 경우(i-1번째 포도주까지 마신 양)
        
        dp.append(li[0])
        dp.append(li[0] + li[1])
        dp.append(max(li[0] + li[2], li[1] + li[2], dp[1]))
        
        for i in range(3, n):
            dp.append(max(dp[i-2] + li[i], dp[i-3] + li[i-1] + li[i], dp[i-1]))
        
        return dp[-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    li = [int(input()) for _ in range(n)]
    
    # output
    print(solution(n, li))