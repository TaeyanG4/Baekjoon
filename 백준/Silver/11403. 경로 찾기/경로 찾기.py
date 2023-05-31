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
# from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def solution(n, mat):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if mat[i][k] and mat[k][j]:
                    mat[i][j] = 1
    
    return mat
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    
    # output
    ans = solution(n, mat)
    for i in ans:
        for j in i:
            print(j, end=' ')
        print()