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

def min(a : list, b : list) -> list:
    if a[0] > b[0]:
        return b
    else:
        return a

def findMinSeg(node, start, end, a, b):
    if start > b or end < a:
        return [INF, INF]
    
    if a <= start and end <= b:
        return tree[node]
    
    mid = (start + end) // 2
    return min(findMinSeg(node*2, start, mid, a, b), findMinSeg(node*2+1, mid+1, end, a, b))

def updateSeg(node, start, end, index, val):
    if index < start or index > end:
        return [INF, INF]
    
    if start == end:
        tree[node] = val
        return
    
    mid = (start + end) // 2
    updateSeg(node*2, start, mid, index, val)
    updateSeg(node*2+1, mid+1, end, index, val)
    tree[node] = min(tree[node*2], tree[node*2+1])

def initSeg(node, start, end):
    if start == end:
        tree[node] = seq[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(initSeg(node*2, start, mid), initSeg(node*2+1, mid+1, end))
    return tree[node]

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    temp = list(map(int, input().split()))
    seq = [[0, 0] for _ in range(n)]
    for i in range(n):
        seq[i][0] = temp[i] # 값
        seq[i][1] = i + 1 # 인덱스
    
    # initSeg
    tree_height = math.ceil(math.log2(n))
    tree_size = 1 << (tree_height + 1)
    tree = [0] * tree_size
    initSeg(1, 0, n-1)
    
    # output
    m = int(input())
    for _ in range(m):
        cmd, a, b = map(int, input().split())
        if cmd == 1:
            seq[a-1][0] = b
            updateSeg(1, 0, n-1, a-1, seq[a-1])
        else:
            print(findMinSeg(1, 0, n-1, a-1, b-1)[1])