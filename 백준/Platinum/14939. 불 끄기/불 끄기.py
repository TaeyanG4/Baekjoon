# import lines
#################################
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

def press(b, y, x):
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 <= ny < 10 and 0 <= nx < 10:
            b[ny][nx] ^= 1

def solution(board):
    
    first_line_press_case = [101] * (1 << 10)
    for case in range(1 << 10):
        cnt = 0
        temp_board = [board[i][:] for i in range(10)]
        
        mask = 1
        for i in range(9, -1, -1):
            if case & mask:
                press(temp_board, 0, i)
                cnt += 1
            mask <<= 1
        
        for i in range(1, 10):
            for j in range(10):
                if temp_board[i-1][j]: # 현재 위치 위에 전구가 켜져있으면
                    press(temp_board, i, j) # 현재 위치 press
                    cnt += 1
        
        if sum(temp_board[9]) == 0:
            first_line_press_case[case] = cnt
                
    
    return min(first_line_press_case)

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    board = [[0] * 10 for _ in range(10)]
    
    for i in range(10):
        line = input().rstrip()
        for j in range(10):
            if line[j] == 'O':
                board[i][j] = 1
    
    # output
    print(solution(board))