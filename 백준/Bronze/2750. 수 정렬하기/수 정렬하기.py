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
    return list(map(int, sorted(list(set(arr)))))

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    t = int(input())
    arr = [int(input()) for _ in range(t)]
    
    # Output
    result = sol(arr)
    for num in result:
        print(num)