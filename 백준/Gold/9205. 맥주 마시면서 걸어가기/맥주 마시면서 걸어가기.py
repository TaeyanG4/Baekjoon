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
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution():
    q = deque()
    q.append((house_x, house_y))
    while q:
        x, y = q.popleft()
        if abs(x - festival_x) + abs(y - festival_y) <= 1000:
            return True
        for i in range(n):
            nx, ny = convenis[i]
            if not visited[i] and abs(nx - x) + abs(ny - y) <= 1000:
                q.append((nx, ny))
                visited[i] = True
    return False

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    t = int(input())
    
    # output
    for _ in range(t):
        n = int(input())
        convenis = []
        visited = [False for _ in range(n)]
        house_x, house_y = map(int, input().split())
        for _ in range(n):
            conveni_x, conveni_y = map(int, input().split())
            convenis.append((conveni_x, conveni_y))
        festival_x, festival_y = map(int, input().split())
        print('happy' if solution() else 'sad')