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

def solution(num, cnt):
    
    global ans
    
    # 가지치기: 이대로 진행해도 갱신 가능성이 없는경우
    if cnt+L-num <= ans:
        return
    
    if num == L:
        ans = max(ans, cnt)
        return
    
    for ci, cj in lst[num]: # 현재 대각선번호에서 가능한 위치 하나씩 놓고 다음 대각선으로..
        if visited[ci-cj] == 0:
            visited[ci-cj] = 1
            solution(num+1, cnt+1) # 놓는경우
            visited[ci-cj] = 0
    solution(num+1, cnt) # 놓지 않는경우
        
if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    lst = [[] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                lst[i+j].append((i, j))
    
    L = 2*n-1
    visited = [0] * (2*n)

    # output
    ans = 0
    solution(0, 0)
    print(ans)