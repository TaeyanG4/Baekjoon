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
# from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def bfs():
    q = deque()
    q.append(n)
    while q:
        s = q.popleft()
        if s == k:
            print(visited[s])
        if 0 <= 2*s <= 100000 and visited[2*s] == -1:
            visited[2*s] = visited[s]
            q.appendleft(2*s)
        if 0 <= s-1 <= 100000 and visited[s-1] == -1:
            visited[s-1] = visited[s] + 1
            q.append(s-1)
        if 0 <= s+1 <= 100000 and visited[s+1] == -1:
            visited[s+1] = visited[s] + 1
            q.append(s+1)

def solution():
    bfs()

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n, k = map(int, input().split())
    visited = [-1] * (100000+1)
    visited[n] = 0

    # ouput
    solution()
