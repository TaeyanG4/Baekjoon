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
from heapq import *
# from itertools import *
# from datetime import datetime
#################################

def solution(x, y, z):
    q = deque()
    q.append((x, y, z))
    
    while q:
        a, b, c = q.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b][c]
        for dx, dy in direction:
            nx, ny = a+dx, b+dy
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and c == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    q.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    q.append((nx, ny, c))
    return -1

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().strip())))
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # ouput
    print(solution(0, 0, 0))