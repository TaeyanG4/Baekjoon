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

def solution(n):
    cnt = 1
    num = 1
    while True:
        if num % n == 0:
            return cnt
        else:
            num = (num*10) + 1
            cnt += 1

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while True:
        try:
            # input
            n = int(input())

        except:
            break
        
        # output
        print(solution(n))
