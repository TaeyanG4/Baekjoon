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
# import pprint
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    mat = [['@'] * (n*5) for _ in range(n*5)]
    for i in range(n, n*5):
        for j in range(n, n*5):
            mat[i][j] = ' '
    
    # output
    for i in range(n*5):
        for j in range(n*5):
            if mat[i][j] == '@':
                print(mat[i][j], end='')
        print()