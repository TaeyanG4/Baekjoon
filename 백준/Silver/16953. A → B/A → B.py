# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
# import statistics as st
# from decimal import *
from collections import *
from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def calc(select, num):
    if select == 0:
        return num * 2
    else:
        return int(str(num)+'1')

def solution(n, m):
    q = deque()
    q.append((n, 1))
    while q:
        now, cnt = q.popleft()
        if now > m:
            continue
        if now == m:
            return cnt
        for i in range(2):
            q.append((calc(i, now), cnt+1))
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, m = map(int, input().split())
    
    # output
    print(solution(n, m))
    