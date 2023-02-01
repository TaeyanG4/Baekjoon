# import line
import sys
import math
import copy
import ast
import re
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *

def sol(v):
    num = []
    for i in v:
        cnt = 0
        s = i.split('+')
        for j in s:
            cnt += int(j)
        num.append(cnt)
    n = num[0]
    for i in range(1, len(num)):
        n -= num[i]
    return n

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    v = input().split('-')
    
    # Output
    print(sol(v))