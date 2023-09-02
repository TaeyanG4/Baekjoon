## taeyang's template (1.0.2)
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
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
#################################

def solution():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    t = int(input())
    
    # output
    for _ in range(t):
        a, b, cnt = map(int, input().split())
        print(f'Data set: {a} {b} {cnt}')
        for _ in range(cnt):
            if a == 0 and b == 0:
                break
            if a > b:
                a //= 2
            else:
                b //= 2
        
        if a < b:
            a, b = b, a
        
        print(a, b)
        print()