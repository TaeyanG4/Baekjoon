## taeyang's template (1.0.8)
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
# from functools import *
#################################


def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    x, y, = S()
    direction_lst = []
    direction_lst.append((x, y))
    for dx, dy in direction:
        direction_lst.append((x + dx, y + dy))
    
    k = int(input())
    cnt = 0
    xx, yy = 0, 0
    
    for i, c in enumerate(input().strip()):
        
        if (xx, yy) in direction_lst:
            print(i)
            cnt += 1
        
        if c == 'S':
            yy += 1
        elif c == 'J':
            yy -= 1
        elif c == 'Z':
            xx -= 1
        elif c == 'I':
            xx += 1
            
    if (xx, yy) in direction_lst:
        print(k)
        cnt += 1
    
    if cnt == 0:
        print(-1)