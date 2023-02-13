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

def sol(arr):
    max_value = -1
    for i in range(9):
        for j in range(9):
            if max_value <max(max_value, arr[i][j]):
                max_value = max(max_value, arr[i][j])
                point = (i+1, j+1)
            
    return max_value, point

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    arr = [list(map(int, input().split())) for _ in range(9)]
    
    # Output
    max_value, point = sol(arr)
    print(max_value)
    print(*point)