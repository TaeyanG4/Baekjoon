## taeyang's template (1.0.4)
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

def solution():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    a, c, e = map(int, input().split())
    x, y, z = map(int, input().split())
    
    # output
    if a <= x and c <= y and e <= z:
        print('A')
    elif a/2 <= x and c <= y and e <= z:
        print('B')
    elif c <= y and e <= z:
        print('C')
    elif c/2 <= y and e <= z:
        print('D')
    else:
        print('E')