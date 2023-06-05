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
# import statistics as st
# from decimal import *
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def dslr(n):
    d = (n * 2) % 10000
    s = n - 1 if n != 0 else 9999
    l = (n % 1000) * 10 + n // 1000
    r = (n % 10) * 1000 + n // 10
    return d, s, l, r

def solution(a, b):
    q = deque()
    q.append((a, ''))
    visited[a] = True
    while q:
        n, path = q.popleft()
        if n == b:
            return path
        for idx, i in enumerate(dslr(n)):
            if not visited[i]:
                visited[i] = True
                if idx == 0:
                    q.append((i, path+'D'))
                if idx == 1:
                    q.append((i, path+'S'))
                if idx == 2:
                    q.append((i, path+'L'))
                if idx == 3:
                    q.append((i, path+'R'))

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    t = int(input())
    
    # output
    for i in range(t):
        visited = [False] * 10000
        a, b = map(int, input().split())
        print(solution(a, b))

