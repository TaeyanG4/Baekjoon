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

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(n, mat, x, y, c):
    
    cnt = 0
    if mat[x][y] == c:
        cnt += 1
    else:
        return 0
    
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and mat[nx][ny] in c:
                q.append((nx, ny))
                mat[nx] = mat[nx][:ny] + 'X' + mat[nx][ny+1:]
                cnt +=1
                
    if cnt > 0:
        return 1
    else:
        return 0

def solution(n, mat):
    
    ans1, ans2 = 0, 0
    mat1 = copy.deepcopy(mat)
    mat2 = copy.deepcopy(mat)
    
    for i in range(n):
        mat2[i] = mat2[i].replace('G', 'R')
    
    for c in 'RGB':
        for i in range(n):
            for j in range(n):
                ans1 += bfs(n, mat1, i, j, c) # 색약이 아닌 사람
        
    for c in 'RB':
        for i in range(n):
            for j in range(n):
                ans2 += bfs(n, mat2, i, j, c) # 색약이 아닌 사람
    
    return ans1, ans2
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    mat = [input().strip() for _ in range(n)]
    
    # output
    print(*solution(n, mat))
    