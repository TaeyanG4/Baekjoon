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

def solution():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    p = int(input())
    
    # output
    n = n // 5
    li = []
    if n == 0:
        li.append(p)
    elif n == 1:
        li.append(p-500)
    elif n == 2:
        li.append(p-500)
        li.append(p-(p//100 * 10))
    elif n == 3:
        li.append(p-(p//100 * 10))
        li.append(p-2000)
    elif n >= 4:
        li.append(p-2000)
        li.append(p-(p//100 * 25))

    ans = min(li)
    if ans > 0:
        print(ans)
    else:
        print(0)