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
    a = int(input())
    x = int(input())
    b = int(input())
    y = int(input())
    t = int(input())
    
    # output
    ans1 = (21 * x * (t - 30)) 
    ans2 = (21 * y * (t - 45))
    if ans1 < 0:
        ans1 = 0
    if ans2 < 0:
        ans2 = 0
    print(ans1 + a, ans2 + b)