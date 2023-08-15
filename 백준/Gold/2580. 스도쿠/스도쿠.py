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

def row_check(row, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
    return True

def col_check(col, num):
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    return True

def square_check(row, col, num):
    nr = (row // 3) * 3
    nc = (col // 3) * 3
    for r in range(3):
        for c in range(3):
            if sudoku[nr + r][nc + c] == num:
                return False
    return True

def dfs(depth):
    if depth == max_depth:
        for row in sudoku:
            print(*row)
        exit(0)
        
    nr, nc = zeros[depth]
    for num in range(1, 10):
        if row_check(nr, num) and col_check(nc, num) and square_check(nr, nc, num):
            sudoku[nr][nc] = num
            dfs(depth + 1)
            sudoku[nr][nc] = 0

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
    max_depth = len(zeros)

    # output
    dfs(0)