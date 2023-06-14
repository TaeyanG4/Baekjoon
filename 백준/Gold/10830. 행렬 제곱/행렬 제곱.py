# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
from heapq import *
# from itertools import *
# from datetime import datetime
#################################

def square(mat1, mat2):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += mat1[i][k] * mat2[k][j]
            res[i][j] %= 1000
    return res

def solution(mat, b):
    if b == 1:
        return mat
    else:
        v = solution(mat, b//2)
        mat_square = square(v, v)
        if b % 2 == 0:
            return mat_square
        else:
            return square(mat_square, mat)

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n, b = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    
    # output
    ans = solution(mat, b)
    for row in ans:
        for elem in row:
            print(elem % 1000, end=' ')
        print()