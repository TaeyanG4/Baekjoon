## import line
import sys
import math
import copy
import ast
import re
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *

## Global Variable
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# n=세로, m=가로
def sol(n, m, l):
    cnt = 0
    arr = [[0] * m for _ in range(n)]
    
    for i, j in l:
        arr[i][j] = 1
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                q = deque()
                q.append((i,j))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                            arr[nx][ny] = 0
                            q.append((nx,ny))
    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        l = [list(map(int, input().split())) for _ in range(k)]
    
        # Output
        print(sol(m, n, l))