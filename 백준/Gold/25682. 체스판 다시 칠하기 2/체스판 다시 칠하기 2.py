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
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
#################################

def solution(n, m, k, board):
    ans = INF
    black_start_pSum = [[0] * (m+1) for _ in range(n+1)]
    white_start_pSum = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(n):
        for j in range(m):
            
            if board[i][j] != black_start[i][j]:
                black_start_pSum[i][j] = black_start_pSum[i][j-1] + black_start_pSum[i-1][j] - black_start_pSum[i-1][j-1] + 1
            else:
                black_start_pSum[i][j] = black_start_pSum[i][j-1] + black_start_pSum[i-1][j] - black_start_pSum[i-1][j-1]
            
            if board[i][j] != white_start[i][j]:
                white_start_pSum[i][j] = white_start_pSum[i][j-1] + white_start_pSum[i-1][j] - white_start_pSum[i-1][j-1] + 1
            else:
                white_start_pSum[i][j] = white_start_pSum[i][j-1] + white_start_pSum[i-1][j] - white_start_pSum[i-1][j-1]
    
    # pprint.pprint(black_start_pSum)
    # pprint.pprint(white_start_pSum)
    
    for i in range(k-1, n):
        for j in range(k-1, m):
            black_start_cnt = black_start_pSum[i][j] - black_start_pSum[i-k][j] - black_start_pSum[i][j-k] + black_start_pSum[i-k][j-k]
            white_start_cnt = white_start_pSum[i][j] - white_start_pSum[i-k][j] - white_start_pSum[i][j-k] + white_start_pSum[i-k][j-k]
            ans = min(ans, black_start_cnt, white_start_cnt)
            
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m, k = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    
    black_start, white_start = [], []
    black_flag, white_flag = True, False
    for i in range(n):
        
        black_temp, white_temp = [], []
        for j in range(m):
            if black_flag:
                black_temp.append('B')
                black_flag = not black_flag
            else:
                black_temp.append('W')
                black_flag = not black_flag
                
            if white_flag:
                white_temp.append('B')
                white_flag = not white_flag
            else:
                white_temp.append('W')
                white_flag = not white_flag
                
        black_start.append(black_temp)
        white_start.append(white_temp)
        if m % 2 == 0:
            black_flag = not black_flag
            white_flag = not white_flag

    # output
    print(solution(n, m, k, board))