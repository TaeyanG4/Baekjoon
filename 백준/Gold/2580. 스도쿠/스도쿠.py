## taeyang's template (1.0.0)
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
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def dfs(depth):
    if depth == max_depth:
        for i in range(9):
            print(*sudoku[i])
        exit(0)
    
    nc, nr = zeros[depth]
    nsq = (nc//3)*3 + nr//3
    for i in range(1, 10):
        if not row[nc][i] and not col[nr][i] and not square[nsq][i]:
            row[nc][i] = True
            col[nr][i] = True
            square[nsq][i] = True
            sudoku[nc][nr] = i
            dfs(depth+1)
            row[nc][i] = False
            col[nr][i] = False
            square[nsq][i] = False

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    sudoku = [[False for _ in range(9)] for _ in range(9)]
    row = [[False for _ in range(10)] for _ in range(9)]
    col = [[False for _ in range(10)] for _ in range(9)]
    square = [[False for _ in range(10)] for _ in range(9)]
    
    zeros = []
    for i in range(9):
        li = [*map(int, input().split())]
        for j in range(9):
            sudoku[i][j] = li[j]
            if li[j]:
                row[i][li[j]] = True
                col[j][li[j]] = True
                square[(i//3)*3 + j//3][li[j]] = True
            else:
                zeros.append((i, j))
    max_depth = len(zeros)
    
    # output
    dfs(0)