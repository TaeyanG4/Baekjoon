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

def sol(l):
    stack = []
    ans = [0] * len(l)
    for i in range(len(l)):
        while stack:
            if stack[-1][1] > l[i]:
                ans[i] = stack[-1][0] + 1
                break
            else:
                stack.pop()
        stack.append([i, l[i]])
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    l = list(map(int, input().split()))
    
    # Output
    print(*sol(l))