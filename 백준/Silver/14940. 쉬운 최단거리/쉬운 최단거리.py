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

mov = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(n, m, li, start):
    q = deque()
    q.append(start)
    while q:
        y, x = q.popleft()
        for dy, dx in mov:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and li[ny][nx] != 0:
                visited[ny][nx] = True
                li[ny][nx] = li[y][x] + 1
                q.append((ny, nx))

def solution(n, m, li):
    
    # find start point
    for i in range(n):
        for j in range(m):
            if li[i][j] == 2:
                start = (i, j)
                visited[i][j] = True
                li[i][j] = 0
                break
    
    # solving
    bfs(n, m, li, start)
    
    # unable to enter is -1
    for i in range(n):
        for j in range(m):
            if li[i][j] == 1 and visited[i][j] == False:
                li[i][j] = -1
    
    # print
    for i in range(n):
        for j in range(m):
            print(li[i][j], end=' ')
        print()

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, m = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    # output
    solution(n, m, li)
    
    