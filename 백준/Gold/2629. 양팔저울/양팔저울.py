## taeyang's template (1.0.1)
# https://source-sc.tistory.com/3
# https://hseungyeon.tistory.com/354
# https://my-coding-notes.tistory.com/157
# https://one10004.tistory.com/287
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
from collections import defaultdict
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
#################################

def dfs(idx, weight):
    if idx > n:
        return
    
    if memo[idx][weight]:
        return
    
    memo[idx][weight] = True
    
    dfs(idx + 1, weight) # 추를 추가하지 않는 경우
    dfs(idx + 1, weight + weights[idx-1]) # 왼쪽에 추를 추가하는 경우
    dfs(idx + 1, abs(weight-weights[idx-1])) # 오른쪽에 추를 추가하는 경우

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    weights = list(map(int, input().split()))
    
    # dfs
    memo = [[False for _ in range((i+1)*500+1)] for i in range(n+1)]
    dfs(0, 0)
    
    # output
    m = int(input())
    for i in map(int, input().split()):
        if i > 500*n:
            print('N', end=' ')
            continue
        if memo[n][i]:
            print('Y', end=' ')
        else:
            print('N', end=' ')