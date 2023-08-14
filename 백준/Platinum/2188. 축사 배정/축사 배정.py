## taeyang's template (1.0.0)
#################################
# https://m.blog.naver.com/hands731/221891105733
# https://www.youtube.com/watch?v=PwXNTA0rpXc&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz&index=33
# https://konghana01.tistory.com/305
# https://hw-seo.tistory.com/entry/백준-2188-축사-배정
# https://m.blog.naver.com/hands731/221891105733
#################################
#################################
## my import lines
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

# 성공시 True, 실패시 False
def solution(x): # dfs
    
    # 연결된 모든 노드에 대해서 들어갈 수 있는지 시도
    for i in cows[x]:
        
        # 이미 처리한 노드는 더 이상 볼 필요 X
        if visited[i]:
            continue
        visited[i] = True
        
        # 비어있거나 점유 노드에 더 들어갈 공간이 있는 경우
        if rooms[i] == 0 or solution(rooms[i]):
            rooms[i] = x
            return True
        
    return False

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    cows = [[] for _ in range(n+1)]
    rooms = [0] * (m+1)
    cnt = 0
    
    for i in range(1, n+1):
        si, *a = map(int, input().split())
        cows[i] = a
    
    for i in range(1, n+1):
        visited = [False] * (m+1)
        if solution(i):
            cnt += 1
    
    # output
    print(cnt)