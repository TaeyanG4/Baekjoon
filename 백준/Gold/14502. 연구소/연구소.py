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
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
#################################

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(mat):
    global max_val
    new_matrix = copy.deepcopy(mat)
    q = deque(viruses)
    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and new_matrix[ny][nx] == 0:
                new_matrix[ny][nx] = 2
                q.append((ny, nx))
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_matrix[i][j] == 0:
                cnt += 1
    max_val = max(max_val, cnt)

def solution(count):
    global max_val
    if count == 3:
        bfs(mat)
        return 
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                mat[i][j] = 1
                solution(count + 1)
                mat[i][j] = 0

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    max_val = 0
    viruses = []
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                viruses.append((i, j))
    
    # ouput
    solution(count = 0)
    print(max_val)