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

def solution(s_month, s_year, e_month, e_year):
    eit = 0
    if s_year == e_year:
        month = e_month - s_month
        eit += (1/2) * (month / (12-s_month+1))
    else:
        eit += 0.5
        eit += (e_year - s_year - 1)
        eit += (1/12) * (e_month - 1)
    
    return round(eit, 4)

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    
    # output
    for i in range(n):
        s_month, s_year = map(int, input().split())
        e_month, e_year = map(int, input().split())
        ans = solution(s_month, s_year, e_month, e_year)
        print(f'{ans:.4f}')