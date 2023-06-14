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


def solution(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i+1][j-1] = stars[i+1][j+1] = '*'
        for k in range(-2, 3):
            stars[i+2][j - k] = '*'
    else:
        next_size = size // 2
        solution(i, j, next_size)
        solution(i+next_size, j-next_size, next_size)
        solution(i+next_size, j+next_size, next_size)

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**5)
    
    # input
    n = int(input())
    stars = [[' ']*2*n for _ in range(n)]

    # output
    solution(0, n-1, n)
    for star in stars:
        print(''.join(star))