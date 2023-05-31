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
# import statistics as st
# from decimal import *
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def conquest(n, mat, i, j, size):
    if size == 1:
        return mat[i][j]
    
    half = size // 2
    a = conquest(n, mat, i, j, half)
    b = conquest(n, mat, i, j+half, half)
    c = conquest(n, mat, i+half, j, half)
    d = conquest(n, mat, i+half, j+half, half)
    
    if a == b == c == d == '0' or a == b == c == d == '1':
        return a
    else:
        return '(' + a + b + c + d + ')'

def solution(n, mat):
    return conquest(n, mat, 0, 0, n)
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    mat = [list(map(str, input().strip())) for _ in range(n)] 
    
    # output
    print(solution(n, mat))
    