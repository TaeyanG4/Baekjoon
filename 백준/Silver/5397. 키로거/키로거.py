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


def sol(s):
    ans = deque()
    cnt = 0
    for c in s:
        if c == "<":
            if cnt != 0:
                cnt -= 1
        elif c == ">":
            if cnt < len(ans):
                cnt += 1
        elif c == "-":
            if 0 <= (cnt-1) < len(ans):
                del ans[cnt-1]
                cnt -= 1
        else:
            ans.insert(cnt, c)
            cnt += 1
    return "".join(list(ans))

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    t = int(input())

    # output
    for i in range(t):
        print(sol(input().rstrip()))
