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
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

# https://ddggblog.tistory.com/211

def solution(start):
    global memo, visited, tree
    
    visited[start] = True
    memo[start][1] += 1 # 자신이 얼리어답터인 경우 자신을 포함
    
    for node in tree[start]:
        if not visited[node]:
            solution(node)
            
            # 자신이 얼리어답터인 경우 자식은 얼리어답터여도 되고 아니여도 됨
            memo[start][1] += min(memo[node])
            
            # 자신이 얼리어답터가 아닌 경우 자식은 얼리어답터여야 함
            memo[start][0] += memo[node][1]

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    tree = defaultdict(list)
    memo = [[0, 0] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    # output
    solution(1)
    print(min(memo[1][0], memo[1][1]))