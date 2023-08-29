## taeyang's template (1.0.1)
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
# import pprint
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
#################################

def solution(l, sx, sy, ex, ey):
    q = deque([(sx, sy, 0)])
    visited[sx][sy] = True
    
    while q:
        x, y, cnt = q.popleft()
        if x == ex and y == ey:
            return cnt
        for dx, dy in knight_directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    t = int(input())
    knight_directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    
    # output
    for _ in range(t):
        l = int(input())
        sx, sy = map(int, input().split())
        ex, ey = map(int, input().split())
        visited = [[False] * l for _ in range(l)]
        print(solution(l, sx, sy, ex, ey))