# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################
# https://johoonday.tistory.com/152
# https://hillier.tistory.com/54
# https://www.youtube.com/watch?v=LQ3JHknGy8c

def find(x):
        global vroot
        if x != vroot[x]:
            vroot[x] = find(vroot[x])
        return vroot[x]

def solution1(v, e, vroot, elist):
    
    # kruskal algorithm
    ans = 0
    elist.sort(key=lambda x: x[2]) # 가중치 기준으로 오름차순 정렬
    for s, e, w in elist:
        sroot = find(s)
        eroot = find(e)
        if sroot != eroot:
            if sroot > eroot:
                vroot[sroot] = eroot
            else:
                vroot[eroot] = sroot
            ans += w
    return ans

# def solution2(v, e, visited, elist):
    
#     # prim algorithm
#     ans, cnt = 0, 0
#     while pq:
#         if cnt == v:
#             break
#         w, s = heappop(pq)
#         if not visited[s]:
#             visited[s] = True
#             ans += w
#             cnt += 1
#             for i in elist[s]:
#                 heappush(pq, i)
#     return ans
    
if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # sloution1 kruskal algorithm
    # input
    v, e = map(int, input().split())
    vroot = [i for i in range(v+1)]
    elist = [] 
    for _ in range(e):
        elist.append(list(map(int, input().split())))
    
    # output
    print(solution1(v, e, vroot, elist))
    
    # # sloution2 prim algorithm
    # # input
    # v, e = map(int, input().split())
    # visited = [False] * (v+1)
    # elist = [[] for _ in range(v+1)]
    # pq = [[0, 1]]
    # for _ in range(e):
    #     s, e, w = map(int, input().split())
    #     elist[s].append([w, e])
    #     elist[e].append([w, s])
    
    # # output
    # print(solution2(v, e, visited, elist))