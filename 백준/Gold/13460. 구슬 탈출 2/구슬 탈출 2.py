# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from itertools import *
from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def solution(board):
    cnt = 0
    visited = set()
    q = deque()
    q.append((Ry, Rx, By, Bx, cnt))
    visited.add((Ry, Rx, By, Bx))
    
    while q:
        ry, rx, by, bx, cnt = q.popleft()
        if board[ry][rx] == 'O':
            return cnt
        
        if cnt >= 10:
            continue
        
        # r, b 움직이기
        for dy, dx in direction:
            
            r_move = 0
            b_move = 0
            
            # r 움직이기
            nry = ry + dy
            nrx = rx + dx
            while True:
                if board[nry][nrx] == '#':
                    nry -= dy
                    nrx -= dx
                    break
                elif board[nry][nrx] == 'O':
                    break
                
                nry += dy
                nrx += dx
                r_move += 1
            
            # b 움직이기
            nby = by + dy
            nbx = bx + dx
            while True:
                if board[nby][nbx] == '#':
                    nby -= dy
                    nbx -= dx
                    break
                elif board[nby][nbx] == 'O':
                    break
                
                nby += dy
                nbx += dx
                b_move += 1
            
            # b가 빠졌을 때
            if board[nby][nbx] == 'O':
                continue
            
            # r, b가 겹쳤을 때
            if nry == nby and nrx == nbx:
                if r_move > b_move:
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx
            
            if not (nry, nrx, nby, nbx) in visited:
                q.append((nry, nrx, nby, nbx, cnt+1))
                visited.add((nry, nrx, nby, nbx))
    return -1

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n, m = map(int, input().split())
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    board = []
    Ry, Rx, By, Bx, = 0, 0, 0, 0
    for i in range(n):
        temp = input().strip()
        board.append(temp)
        if 'R' in temp:
            Ry, Rx = i, temp.index('R')
        if 'B' in temp:
            By, Bx = i, temp.index('B')
            
    # output
    print(solution(board))