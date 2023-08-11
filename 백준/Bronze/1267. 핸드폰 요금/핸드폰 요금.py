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

def solution(n, li):
    price_y, price_m = 0, 0
    for i in li:
        price_y += (i//30 + 1) * 10
        price_m += (i//60 + 1) * 15
    
    if price_y < price_m:
        return 'Y', price_y
    elif price_y > price_m:
        return 'M', price_m
    else:
        return 'Y', 'M', price_y

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    li = list(map(int, input().split()))
    
    # output
    print(*solution(n, li))