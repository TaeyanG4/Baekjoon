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

def sol(li):
    li.sort(key=lambda x: x[0])
    cnt = 1
    temp = li[0][1]
    for a, b in li:
        if b < temp:
            cnt += 1
            temp = b
    return cnt
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    t = int(input())
    
    # output
    for _ in range(t):
        n = int(input())
        li = list()
        for _ in range(n):
            a, b = map(int, input().split())
            li.append((a, b))
        print(sol(li))
