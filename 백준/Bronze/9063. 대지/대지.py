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

def solution(n, x_arr, y_arr):
    if n == 1:
        return 0
    else:
        x_val = max(x_arr) - min(x_arr)
        y_bal = max(y_arr) - min(y_arr)
        return x_val * y_bal

if __name__ == '__main__':
    # input = sys.stdin.readline
    
    # input
    n = int(input())
    x_arr, y_arr = list(), list()
    for i in range(n):
        x, y = map(int, input().split())
        x_arr.append(x)
        y_arr.append(y)
    
    # output
    print(solution(n, x_arr, y_arr))