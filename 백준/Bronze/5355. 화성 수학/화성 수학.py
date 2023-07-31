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

def solution(li):
    v = float(li[0])
    for i in li[1:]:
        if i == '@':
            v *= 3
        elif i == '%':
            v += 5
        elif i == '#':
            v -= 7
    return v

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    t = int(input().strip())
    
    # output
    for _ in range(t):
        li = list(map(str, input().split()))
        v = solution(li)
        print(f'{v:.2f}')