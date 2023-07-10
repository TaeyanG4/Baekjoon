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
# import pprint
# from collections import *
# from itertools import *
# from statistics import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def move(mat, dirction):
    if dirction == 'up':
        for i in range(n):
            p = 0
            for j in range(1, n):
                if mat[j][i]:
                    temp, mat[j][i] = mat[j][i], 0
                    
                    # 포인터가 가리키는 값이 0이면
                    if not mat[p][i]:
                        mat[p][i] = temp
                    # 포인터가 가리키는 값이 현재 값과 같으면
                    elif mat[p][i] == temp:
                        mat[p][i] *= 2
                        p += 1
                    # 포인터가 가리키는 값이 현재 값과 다르면
                    else:
                        p += 1
                        mat[p][i] = temp
    elif dirction == 'down':
        for i in range(n):
            p = n-1
            for j in range(n-2, -1, -1):
                if mat[j][i]:
                    temp, mat[j][i] = mat[j][i], 0
                    if not mat[p][i]:
                        mat[p][i] = temp
                    elif mat[p][i] == temp:
                        mat[p][i] *= 2
                        p -= 1
                    else:
                        p -= 1
                        mat[p][i] = temp
    
    elif dirction == 'left':
        for i in range(n):
            p = 0
            for j in range(1, n):
                if mat[i][j]:
                    temp, mat[i][j] = mat[i][j], 0
                    if not mat[i][p]:
                        mat[i][p] = temp
                    elif mat[i][p] == temp:
                        mat[i][p] *= 2
                        p += 1
                    else:
                        p += 1
                        mat[i][p] = temp
    else:
        for i in range(n):
            p = n-1
            for j in range(n-2, -1, -1):
                if mat[i][j]:
                    temp, mat[i][j] = mat[i][j], 0
                    if not mat[i][p]:
                        mat[i][p] = temp
                    elif mat[i][p] == temp:
                        mat[i][p] *= 2
                        p -= 1
                    else:
                        p -= 1
                        mat[i][p] = temp
    return mat

def solution(mat, cnt):
    
    global max_val
    if cnt == 5:
        max_val = max(max(map(max, mat)), max_val)
        return
    else:
        for d in direction:
            temp_mat = move(copy.deepcopy(mat), d)
            solution(temp_mat, cnt+1)

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    direction = ['up', 'down', 'left', 'right']
    max_val = 0
    
    # output
    solution(mat, 0)
    print(max_val)