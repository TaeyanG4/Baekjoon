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

def find(x):
    if alters[x] == x:
        return x
    else:
        alters[x] = find(alters[x])
        return alters[x]

def union(root):
    alters[root] = find(root - 1)

def solution(g, p):
    
    cnt = 0
    for i in range(p):
        root = find(int(input()))
        if root == 0:
            break
        union(root)
        cnt += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    g = int(input())
    p = int(input())
    alters = list(range(g + 1))
    
    # output
    print(solution(g, p))