# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################

def row_check(r, n):
    for x in range(9):
        if sdoku[r][x] == n:
            return False
    return True

def col_check(c, n):
    for x in range(9):
        if sdoku[x][c] == n:
            return False
    return True

def square_check(r, c, n):
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    for r in range(3):
        for c in range(3):
            if sdoku[nr+r][nc+c] == n:
                return False
    return True

def dfs(depth):
    if depth >= len(zero):
        for row in sdoku:
            print(*row, sep='')
        exit()

    nr, nc = zero[depth]
    for i in range(1, 10):
        if row_check(nr, i) and col_check(nc, i) and square_check(nr, nc, i):
            sdoku[nr][nc] = i
            dfs(depth+1)
            sdoku[nr][nc] = 0
            
if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    sdoku = [list(map(int, str(input().strip()))) for _ in range(9)]
    zero = [(i, j) for i in range(9) for j in range(9) if sdoku[i][j] == 0]
    
    # output
    dfs(0)