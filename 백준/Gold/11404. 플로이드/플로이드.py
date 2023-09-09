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
# from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def solution():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = int(input())
    m = int(input())
    graph = [[sys.maxsize] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        if graph[a-1][b-1] > c:
            graph[a-1][b-1] = c
    
    # ouput
    solution()
    for i in graph:
        for j in i:
            if j == sys.maxsize:
                print(0, end=' ')
            else:
                print(j, end=' ')
        print()
