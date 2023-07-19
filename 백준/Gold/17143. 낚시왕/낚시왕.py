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
import pprint
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def move_shark():
    global r, c, m, shark_info
    
    new_mat = [[0] * (c) for _ in range(r)]
    new_shark_info = defaultdict(list)
    
    for z in shark_info.keys():
        y, x, spd, d, siz  = shark_info[z]
        
        if d == 1 or d == 2:
            s = spd % ((r-1) * 2)
        else:
            s = spd % ((c-1) * 2)
        
        while s:

            dy, dx = direction[d]
            ny, nx = y + dy, x + dx
            
            if 0 <= ny < r and 0 <= nx < c:
                y, x = ny, nx
                s -= 1
            else:
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                elif d == 4:
                    d = 3
            
        if new_mat[y][x] == 0:
            new_mat[y][x] = siz
            new_shark_info[siz] = (y, x, spd, d, siz)
        else:
            if new_mat[y][x] < siz:
                new_shark_info.pop(new_mat[y][x])
                new_shark_info[siz] = (y, x, spd, d, siz)
                new_mat[y][x] = siz
    
    return new_mat, new_shark_info

def fishing(x):
    global r, c, m, mat
    
    for y in range(r):
        
        if mat[y][x] != 0:
            
            # 상어 잡기
            z = mat[y][x]
            mat[y][x] = 0
            shark_info.pop(z)
            return z
        
    return 0

def solution():
    global r, c, m, mat, shark_info
    
    ans = 0
    cnt = 0
    
    while True:
        if cnt == c:
            break
        
        # 낚시하기
        ans += fishing(cnt)
        
        # 상어 이동
        mat, shark_info = move_shark()
        cnt += 1
        
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    direction = {1:(-1, 0), 2:(1, 0), 3:(0, 1), 4:(0, -1)} # 위, 아래, 오른쪽, 왼쪽
    
    # input
    r, c, m = map(int, input().split())
    mat = [[0] * (c) for _ in range(r)]
    shark_info = defaultdict(list)
    for _ in range(m):
        i, j, s, d, z = map(int, input().split())
        mat[i-1][j-1] = z
        shark_info[z] = (i-1, j-1, s, d, z)
    
    # output
    print(solution())