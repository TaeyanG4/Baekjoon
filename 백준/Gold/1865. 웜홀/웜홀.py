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
from heapq import *
# from itertools import *
# from datetime import datetime
#################################

def solution():
    for i in range(n):
        for j in range(len(edges)):
            cur, cost, nxt = edges[j]
            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                if i == n-1:
                    return True
    return False

if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**9)
    
    # input
    t = int(input())

    # ouput
    for i in range(t):
        n, m, w = map(int, input().split())
        dist = [sys.maxsize] * (n+1)
        edges = []
        
        for i in range(m):
            s, e, t = map(int, input().split())
            edges.append((s, t, e))
            edges.append((e, t, s))
            
        for i in range(w):
            s, e, t = map(int, input().split())
            edges.append((s, -t, e))

        if solution():
            print('YES')
        else:
            print('NO')
