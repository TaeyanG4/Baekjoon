# import lines
#################################
import sys
# import math
# import copy
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

def solution(mat):
    max_val = 0
    for y in range(n):
        for x in range(n):
            
            if max_val == n:
                return max_val
            
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n:
                    t, b, l, r = 0, 0, 0, 0
                    mat[y][x], mat[ny][nx] = mat[ny][nx], mat[y][x]
                    
                    while x-l >= 0 and mat[y][x] == mat[y][x-l]: 
                        l += 1
                    while x+r < n and mat[y][x] == mat[y][x+r]:
                        r += 1
                    while y-t >= 0 and mat[y][x] == mat[y-t][x]:
                        t += 1
                    while y+b < n and mat[y][x] == mat[y+b][x]:
                        b += 1
                    
                    mat[y][x], mat[ny][nx] = mat[ny][nx], mat[y][x]
                    max_val = max(max_val, t+b-1, l+r-1)
                    
    return max_val

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n = int(input())
    mat = [list(input()) for _ in range(n)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # output
    print(solution(mat))