# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def mul_mat(n, m, k, mat1, mat2):
    new_mat = [[0 for _ in range(k)] for _ in range(n)]
    for i in range(n):
        for j in range(k):
            for l in range(m):
                new_mat[i][j] += mat1[i][l] * mat2[l][j]
    return new_mat

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n, m = map(int, input().split())
    mat1 = [list(map(int, input().split())) for _ in range(n)]
    m, k = map(int, input().split())
    mat2 = [list(map(int, input().split())) for _ in range(m)]
    
    # output
    new_mat = mul_mat(n, m, k, mat1, mat2)
    for i in new_mat:
        print(*i)