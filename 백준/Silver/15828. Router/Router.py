# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

# 0 = queue , 1 = stack
def sol(buffer):
    ans = deque()
    while True:
        v = int(input())
        if v == -1:
            break
        if v == 0:
            ans.popleft()
        elif len(ans) < buffer and v != -1:
            ans.append(v)
    
    if len(ans) == 0:
        return "empty"
    else:
        return list(ans)
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    buffer = int(input())

    # output
    print(*sol(buffer))
