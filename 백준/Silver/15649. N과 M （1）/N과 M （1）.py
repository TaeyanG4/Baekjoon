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
from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(cnt):
    if cnt == m:
        print(*temp)
        return
    else:
        for i in range(1, n + 1):
            if i in temp:
                continue
            temp.append(i)
            solution(cnt + 1)
            temp.pop()
    

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    # INF = sys.maxsize
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, m = map(int, input().split())
    temp = []
    
    # output
    solution(0)