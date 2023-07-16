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

def distance(houses_li, chiken_li):
    min_val = 0
    for house in houses_li:
        temp = INF
        for chicken in chiken_li:
            temp = min(temp, abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
        min_val += temp
    return min_val
    
def solution(houses, chikens):
    global min_dist
    for chiken_m in combinations(chikens, m):
        min_dist = min(min_dist, distance(houses, chiken_m))

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m  = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    
    houses, chikens = [], []
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                houses.append((i, j))
            elif mat[i][j] == 2:
                chikens.append((i, j))
    
    min_dist = INF
    
    # output
    solution(houses, chikens)
    print(min_dist)