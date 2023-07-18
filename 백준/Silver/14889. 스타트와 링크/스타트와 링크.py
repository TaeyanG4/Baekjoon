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
from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n, mat):
    ans = INF
    row, col = [sum(i) for i in mat], [sum(i) for i in zip(*mat)]
    new_mat = [i+j for i, j in zip(row, col)]
    total_sum = sum(new_mat) // 2
    for combi in combinations(new_mat, n//2):
        ans = min(ans, abs(total_sum-sum(combi)))
        if not ans:
            break
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    
    # output
    print(solution(n, mat))