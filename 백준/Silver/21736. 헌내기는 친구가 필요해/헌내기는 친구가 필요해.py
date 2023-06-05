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

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(n, m, li, start):
    global cnt
    q = deque()
    q.append(start)
    while q:
        y, x = q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and li[ny][nx] != 'X':
                if li[ny][nx] == 'P':
                    cnt += 1
                    li[ny][nx] = 'X'
                    q.append((ny, nx))
                elif li[ny][nx] == 'O':
                    li[ny][nx] = 'X'
                    q.append((ny, nx))


def solution(n, m, li):
    for i in range(n):
        for j in range(m):
            if li[i][j] == 'I':
                me = (i, j)
                break
    
    bfs(n, m, li, me)

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, m = map(int, input().split())
    li = [[c for c in input().strip()] for _ in range(n)]
    cnt = 0
    
    # output
    solution(n, m, li)
    if cnt == 0:
        print('TT')
    else:
        print(cnt)
    
    