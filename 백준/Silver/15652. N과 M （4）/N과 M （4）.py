# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
# import pprint
# import statistics as st
# from decimal import *
from collections import *
from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def dfs(start, cnt):
    if cnt == m:
        ans.append(temp.copy())
        return
    
    for i in range(start, n+1):
        temp.append(i)
        dfs(i, cnt+1)
        temp.pop()

def solution(n, m):
    dfs(1, 0)
    
    # output line
    for i in ans:
        for j in i:
            print(j, end=' ')
        print()

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, m = map(int, input().split())
    ans, temp = list(), list()
    cnt = 0
    
    # output
    solution(n, m)