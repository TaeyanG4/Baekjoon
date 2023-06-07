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

def solution(cnt):
    if cnt == m:
        visited_val.append(copy.deepcopy(tuple(temp)))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            temp.append(li[i])
            solution(cnt+1)
            visited[i] = False
            temp.pop()
            
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort()
    visited = [False] * n
    visited_val = []
    cnt, temp = 0, []
    
    # output
    
    solution(0)
    for i in sorted(list(set(visited_val))):
        print(*i)
    