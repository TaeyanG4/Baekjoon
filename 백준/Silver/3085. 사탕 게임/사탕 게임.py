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
# from collections import *
# from itertools import *
# from statistics import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def checker(mat):
    max_val = 1
    for r in mat:
        if max_val == n:
            return max_val
        
        cnt = 1
        for i in range(n-1):
            if r[i] == r[i+1]:
                cnt += 1
            else:
                max_val = max(max_val, cnt)
                cnt = 1
        else:
            max_val = max(max_val, cnt)

    for c in zip(*mat):
        if max_val == n:
            return max_val
        
        cnt = 1
        for i in range(n-1):
            if c[i] == c[i+1]:
                cnt += 1
            else:
                max_val = max(max_val, cnt)
                cnt = 1
        else:
            max_val = max(max_val, cnt)
            
    return max_val

def solution():
    global mat
    max_val = 0
    
    for i in range(n):
        for j in range(n-1):
            if max_val == n:
                return max_val
            else:
                mat[i][j], mat[i][j+1] = mat[i][j+1], mat[i][j]
                max_val = max(max_val, checker(mat))
                mat[i][j], mat[i][j+1] = mat[i][j+1], mat[i][j]
    
    for i in range(n-1):
        for j in range(n):
            if max_val == n:
                return max_val
            else:
                mat[i][j], mat[i+1][j] = mat[i+1][j], mat[i][j]
                max_val = max(max_val, checker(mat))
                mat[i][j], mat[i+1][j] = mat[i+1][j], mat[i][j]
    
    return max_val

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n = int(input())
    mat = [list(input().rstrip()) for _ in range(n)]
    
    # output
    print(solution())
