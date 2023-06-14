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
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += mat1[i][k] * mat2[k][j]
            res[i][j] %= 1000000007
    return res

def solution(mat, n):
    if n == 1:
        return mat
    else:
        v = solution(mat, n//2)
        mat_square = square(v, v)
        if n % 2 == 0:
            return mat_square
        else:
            return square(mat_square, mat)

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**5)
    
    # input
    n = int(input())
    mat = [[1, 1], [1, 0]]
    
    # output
    ans = solution(mat, n)
    print(ans[0][1] % 1000000007)