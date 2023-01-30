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

def sol(x, n, l):
    sum = 0
    for price, item in l:
        sum += price * item
    if sum == x:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    x, n = int(input()), int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    
    # Output
    print(sol(x, n, l))