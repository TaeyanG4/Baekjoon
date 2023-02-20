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

def recursion(s, start, end):
    global cnt
    cnt += 1
    if start >= end:
        return 1
    elif s[start] != s[end]:
        return 0
    else:
        return recursion(s, start+1, end-1)

def sol(s):
    return recursion(s, 0, len(s)-1)

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    t = int(input())
    
    # output
    for i in range(t):
        cnt = 0
        s = input().strip()
        print(sol(s), cnt)
