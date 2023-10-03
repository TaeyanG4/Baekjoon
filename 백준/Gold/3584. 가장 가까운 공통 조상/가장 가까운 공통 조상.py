## taeyang's template (1.0.7)
#################################
# https://ddiyeon.tistory.com/8
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

def lca(a, b):
    parentA, parentB = [a], [b]
    
    while parent[a]:
        parentA.append(parent[a])
        a = parent[a]
    
    while parent[b]:
        parentB.append(parent[b])
        b = parent[b]
    
    levelA, levelB = len(parentA) - 1, len(parentB) - 1
    while parentA[levelA] == parentB[levelB]:
        levelA -= 1
        levelB -= 1
    
    return parentA[levelA + 1]

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    t = int(input()) # test case

    for _ in range(t):
        
        # input
        n = int(input()) # node count
        parent = [0 for i in range(n + 1)]
        for _ in range(n - 1):
            a, b = map(int, input().split())
            parent[b] = a
        
        targetA, targetB = map(int, input().split())
        
        # output
        print(lca(targetA, targetB))