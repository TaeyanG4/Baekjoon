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
from itertools import *
# from datetime import datetime
#################################

def distance(house_li, chicken_li):
    min_val = 0
    for h in house_li:
        temp = sys.maxsize
        for c in chicken_li:
            temp = min(temp, abs(c[0]-h[0])+abs(c[1]-h[1]))
        min_val += temp
    return min_val

def solution(cnt):
    global dist
    for v in combinations(chicken, m):
        dist = min(dist, distance(house, v))

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**5)
    
    # input
    n, m = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]
    dist = sys.maxsize
    
    chicken, house = [], []
    for i in range(n):
        for j in range(n):
            if li[i][j] == 2:
                chicken.append((i, j))
            if li[i][j] == 1:
                house.append((i, j))
    
    # output
    solution(0)
    print(dist)
    