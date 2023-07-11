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

def solution(r, c, mat):
    
    # 큰 사각형 경계 찾기
    totalCream, msquare, nsquare = 0, 0, 0
    min_x = min_y = 11
    max_x = max_y = -11
    first_x = first_y = -1
    
    for i in range(r):
        for j in range(c):
            if mat[i][j] == '#':
                totalCream += 1
                if first_x == -1:
                    first_x, first_y = i, j
                min_x, min_y = min(min_x, i), min(min_y, j)
                max_x, max_y = max(max_x, i), max(max_y, j)
    
    # '#'이 없으면 하트가 안됨
    if first_x == -1 and first_y == -1: 
        return 0
    
    # 큰 사각형이 정사각형이 아닌경우
    msquare = max_x - min_x + 1
    if max_y - min_y + 1 != msquare:
        return 0
    
    # 작은 사각형 경계 찾기
    m_cream, n_cream  = 0, 0
    min_nx = min_ny = 11
    max_nx = max_ny = -11
    first_nx = first_ny = -1
    
    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            if mat[i][j] == '#':
                m_cream += 1
            else:
                if first_nx == -1:
                    first_nx, first_ny = i, j
                min_nx, min_ny = min(min_nx, i), min(min_ny, j)
                max_nx, max_ny = max(max_nx, i), max(max_ny, j)
                n_cream += 1

    # '.'이 없으면 하트가 안됨
    if first_nx == -1 and first_ny == -1:
        return 0
    
    # 모서리에 작은 사각형 경계가 없으면 하트가 안됨
    if not ((min_nx == min_x and min_ny == min_y) or 
            (min_nx == min_x and max_ny == max_y) or 
            (max_nx == max_x and min_ny == min_y) or 
            (max_nx == max_x and max_ny == max_y)):
        return 0
    
    # 작은 사각형이 정사각형이 아닌경우
    nsquare = max_nx - min_nx + 1
    if max_ny - min_ny + 1 != nsquare:
        return 0
    if totalCream != msquare*msquare - nsquare*nsquare:
        return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    t = int(input().strip())
    
    # output
    for _ in range(t):
        r, c = map(int, input().split())
        mat = [list(input().rstrip()) for _ in range(r)]
        print(solution(r, c, mat))

