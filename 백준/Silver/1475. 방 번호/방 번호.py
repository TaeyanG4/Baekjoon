## import line
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

def sol(s):
    cnt = [0] * 10
    for c in s:
        cnt[int(c)] += 1
    cnt[6] += cnt.pop(9)
    cnt[6] /= 2
    cnt[6] = math.ceil(cnt[6])
    return max(cnt)

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    s = input().strip()
    
    # Output
    print(sol(s))