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

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    
    for i in range(start, n+1):
        temp.append(i)
        dfs(i)
        temp.pop()

def solution(n, m):
    dfs(1)

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, m = map(int, input().split())
    temp = list()
    
    # output
    solution(n, m)