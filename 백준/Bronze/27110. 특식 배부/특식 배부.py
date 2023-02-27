# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import pprint
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def solution(n, a, b, c):
    ans = [n, n, n]
    
    if ans[0] > a:
        ans[0] = a
    if ans[1] > b:
        ans[1] = b
    if ans[2] > c:
        ans[2] = c
    
    return sum(ans)
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = int(input())
    a, b, c = map(int, input().split())

    # output
    print(solution(n, a, b, c))