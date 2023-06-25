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
from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def dfs(x):
    global res
    visited[x] = True
    cycle_li.append(x)
    num = li[x]
    
    if visited[num]: # 방문가능한 곳이 끝났는지
        if num in cycle_li: # 사이클 가능 여부
            res += cycle_li[cycle_li.index(num):] # 사이클 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(num)

if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    
    # input
    t = int(input())
    
    # output
    for _ in range(t):
        n = int(input())
        li = [0] + list(map(int, input().split()))
        visited = [False] * (n+1)
        res = []
        
        for i in range(1, n+1):
            if not visited[i]:
                cycle_li = []
                dfs(i)
        print(n - len(res))