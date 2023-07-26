# import lines
#################################
import sys
# import math
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

def solution(y, x):
    if visited[y][x]: 
        return visited[y][x]

    visited[y][x] = 1
    for dy, dx in direction:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < n and forest[y][x] < forest[ny][nx]:
            visited[y][x] = max(visited[y][x], solution(ny, nx) + 1)
    
    return visited[y][x]

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    forest = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    
    # output
    for i in range(n):
        for j in range(n):
            solution(i, j)
    print(max(map(max, visited)))