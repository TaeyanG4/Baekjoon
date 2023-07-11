# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
# import time
import pprint
from collections import *
# from itertools import *
# from statistics import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def bfs(h, w, board, keys, start, res):
    q = deque()
    visited = [[False] * w for _ in range(h)]
    q.append(start)
    visited[start[0]][start[1]] = True
    
    if board[start[0]][start[1]] == '$':
        res += 1
        board[start[0]][start[1]] = '.'
    elif board[start[0]][start[1]].isupper():
        if board[start[0]][start[1]].lower() in keys:
            board[start[0]][start[1]] = '.'
    elif board[start[0]][start[1]].islower():
        keys.add(board[start[0]][start[1]])
        board[start[0]][start[1]] = '.'
    
    while q:
        y, x = q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny][nx] and board[ny][nx] != '*':
                    
                    if board[ny][nx] == '.':
                        visited[ny][nx] = True
                        q.append((ny, nx))
                    elif board[ny][nx] == '$':
                        visited[ny][nx] = True
                        res += 1
                        q.append((ny, nx))
                        board[ny][nx] = '.'
                    elif board[ny][nx].isupper():
                        visited[ny][nx] = True
                        if board[ny][nx].lower() in keys:
                            q.append((ny, nx))
                            board[ny][nx] = '.'
                    elif board[ny][nx].islower():
                        visited[ny][nx] = True
                        keys.add(board[ny][nx])
                        q.append((ny, nx))
                        board[ny][nx] = '.'
    return res

def solution(h, w, board, keys):
    
    ans = 0
    enterace = deque()
    up_alpha = []
    y, x, dir_cnt = 0, 0, 0
    border = h*2 + w*2 - 4
    while border:
        if 0 <= y < h and 0 <= x < w:
            if board[y][x] == '.':
                enterace.append((y, x))
            if board[y][x] == '$':
                enterace.append((y, x))
            if board[y][x].isupper():
                if board[y][x].lower() in keys:
                    board[y][x] = '.'
                    enterace.append((y, x))
                else:
                    up_alpha.append((y, x))
            if board[y][x].islower():
                keys.add(board[y][x])
                enterace.append((y, x))
                board[y][x] = '.'
            
            y += direction[dir_cnt][0]
            x += direction[dir_cnt][1]
            border -= 1
        else:
            y -= direction[dir_cnt][0]
            x -= direction[dir_cnt][1]
            border += 1
            dir_cnt += 1
    
    flag = True
    cnt = 0
    while flag and enterace:
        start = enterace.popleft()
        enterace.append(start)
        board_temp = copy.deepcopy(board)

        ans = bfs(h, w, board, keys, start, ans)
        
        for a in up_alpha:
            if board[a[0]][a[1]].lower() in keys:
                board[a[0]][a[1]] = '.'
                enterace.append(a)
        
        if board_temp == board:
            if cnt > len(enterace):
                flag = False
            else:
                cnt += 1
        else:
            cnt = 0
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    t = int(input())
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # output
    for i in range(t):
        h, w = map(int, input().split())
        board = [list(input().rstrip()) for _ in range(h)]
        keys = set(input().rstrip())
        
        for i in range(h):
            for j in range(w):
                if board[i][j].isupper():
                    if board[i][j].lower() in keys:
                        board[i][j] = '.'
        
        print(solution(h, w, board, keys))
