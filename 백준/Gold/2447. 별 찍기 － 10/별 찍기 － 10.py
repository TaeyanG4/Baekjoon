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

def solution(si, ei, sj, ej, n):
    global stars
    
    if n == 1:
        return
    
    n = n//3
    for i in range(si+n, ei-n):
        for j in range(sj+n, ej-n):
            stars[i][j] = ' '
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            solution(si+n*i, si+n*(i+1), sj+n*j, sj+n*(j+1), n)

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n = int(input())
    stars = [['*' for _ in range(n)] for _ in range(n)]
    
    # output
    solution(0, n, 0, n, n)
    for star in stars:
        print(''.join(star))