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

# 구간에서 최솟값과 최댓값 찾기
def findSeg(node, start, end, a, b):
    # 탐색 범위 start~end가 구간 a~b와 겹치지 않는 경우
    if a > end or b < start:
        return INF
    
    if a <= start and end <= b:
        return tree[node]
    else:
        mid = (start + end) // 2
        left = findSeg(node*2, start, mid, a, b)
        right = findSeg(node*2+1, mid+1, end, a, b)
        return min(left, right)

# 세그먼트 트리 초기화
def initSeg(node, start, end):
    if start == end:
        tree[node] = li[start]
        return tree[node]
    
    mid = (start + end) // 2
    
    left = initSeg(node*2, start, mid)
    right = initSeg(node*2+1, mid+1, end)
    
    tree[node] = min(left, right)
    return tree[node]

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    li = [int(input()) for _ in range(n)]
    
    tree_height = math.ceil(math.log2(n))
    tree_size = 1 << (tree_height + 1)
    tree = [0] * tree_size
    initSeg(1, 0, n-1)
    
    # output
    for _ in range(m):
        a, b = map(int, input().split())
        print(findSeg(1, 0, n-1, a-1, b-1))