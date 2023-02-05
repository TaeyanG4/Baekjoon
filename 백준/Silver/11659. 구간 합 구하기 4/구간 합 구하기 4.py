# import line
#################################
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
#################################

def sol(arr, i, j):
    
    # S[i,j] = S[1,j] - S[1,i-1]
    return arr[j]-arr[i-1]

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    arr = [0]
    for x in k:
        arr.append(arr[-1]+x)
    
    # Output
    for _ in range(m):
        i, j = map(int, input().split())
        print(sol(arr, i, j))
