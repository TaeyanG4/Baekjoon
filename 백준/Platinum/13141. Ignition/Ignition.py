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

# https://velog.io/@front/백준-Ignition-13141-kpwbnuo4
# https://everenew.tistory.com/169

def init_floyd_warshall(distance):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance

def solution(distance, longest_distance):
    ans = INF
    for s in range(1, n+1):
        temp = 0
        for m in range(1, n+1):
            for e in range(1, n+1):
                if distance[m][e] == INF:
                    continue
                remainLen = longest_distance[m][e] - (distance[s][e] - distance[s][m])
                if remainLen:
                    temp = max(temp, remainLen/2 + distance[s][e])
        ans = min(ans, temp)
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    distance = [[INF] * (n+1) for _ in range(n+1)]
    longest_distance = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        distance[i][i] = 0
    
    for _ in range(m):
        s, e, l = map(int, input().split())
        distance[s][e] = min(distance[s][e], l)
        distance[e][s] = distance[s][e]
        
        longest_distance[s][e] = max(longest_distance[s][e], l)
        longest_distance[e][s] = longest_distance[s][e]
        
    # Floyd-Warshall
    distance = init_floyd_warshall(distance)
    
    # output
    print(solution(distance, longest_distance))