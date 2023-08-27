## taeyang's template (1.0.1)
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
    a, b, n = map(int, input().split())
    
    if n == 0 and a == b:
        print('YES')
    elif (a+b) % 2 == 0:
        a_temp = a - n
        b_temp = b + n
        if a_temp >= b_temp:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')