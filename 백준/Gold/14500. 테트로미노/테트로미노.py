# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
# import pprint
# import statistics as st
# from decimal import *
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
#################################

p = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(mat_sum, i, j, cnt):
    global max_val
    if cnt == 4:
        max_val = max(max_val, mat_sum)
        return
    
    for n in range(4):
        ni, nj = i + p[n][0], j + p[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            if not visited[ni][nj]:
                visited[ni][nj] = True
                dfs(mat_sum + mat[ni][nj], ni, nj, cnt+1)
                visited[ni][nj] = False

def exce(i, j):
    global max_val
    for n in range(4):
        tmp = mat[i][j]
        for k in range(3):
            t = (n+k) % 4
            ni, nj = i + p[t][0], j + p[t][1]
            
            if not (0 <= ni < N and 0 <= nj < M):
                tmp =0
                break
            
            tmp += mat[ni][nj]
        
        max_val = max(max_val, tmp)
            

def solution(N, M):
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(mat[i][j], i, j, 1)
            visited[i][j] = False
            exce(i, j)
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    max_val = 0
    
    # output
    solution(N, M)
    print(max_val)
    