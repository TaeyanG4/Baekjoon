## taeyang's template (1.0.4)
# https://mingchin.tistory.com/427
# https://daekyojeong.github.io/posts/BOJ54/
#################################
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

def find_dp(p1, p2):
    
    # 종료 조건
    if p1 == w or p2 == w:
        return 0
    
    # 만약 이미 계산한 값이라면 그 값을 반환
    if memo[p1][p2] != -1:
        return memo[p1][p2]
    
    # 두 차의 위치
    y1, x1 = car1[p1]
    y2, x2 = car2[p2]
    
    # 다음 차의 위치
    nxt = max(p1, p2) + 1
    
    # 다음 차의 위치에서 두 차가 각각 이동할 때의 거리
    dist1 = abs(y1 - cases[nxt-1][0]) + abs(x1 - cases[nxt-1][1])
    dist2 = abs(y2 - cases[nxt-1][0]) + abs(x2 - cases[nxt-1][1])
    
    # 가까운 거리를 선택
    memo[p1][p2] = min(find_dp(nxt, p2) + dist1, find_dp(p1, nxt) + dist2)
    
    return memo[p1][p2]

def find_path(p1, p2):
    
    # 종료 조건
    if p1 == w or p2 == w:
        return
    
    # 두 차의 위치
    y1, x1 = car1[p1]
    y2, x2 = car2[p2]
    
    # 다음 차의 위치
    nxt = max(p1, p2) + 1
    
    # 다음 차의 위치에서 두 차가 각각 이동할 때의 거리
    dist1 = abs(y1 - cases[nxt-1][0]) + abs(x1 - cases[nxt-1][1])
    dist2 = abs(y2 - cases[nxt-1][0]) + abs(x2 - cases[nxt-1][1])
    
    if memo[nxt][p2] + dist1 < memo[p1][nxt] + dist2:
        print(1)
        find_path(nxt, p2)
    else:
        print(2)
        find_path(p1, nxt)

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, w = int(input()), int(input())
    memo = [[-1] * (w + 1) for _ in range(w + 1)]
    car1, car2 = [(1, 1)], [(n, n)]
    cases = []
    for _ in range(w):
        case = tuple(map(int, input().split()))
        cases.append(case)
        car1.append(case)
        car2.append(case)
    
    # output
    print(find_dp(0, 0)) # car1, car2의 위치를 0으로 초기화
    find_path(0, 0) # car1, car2의 위치를 0으로 초기화