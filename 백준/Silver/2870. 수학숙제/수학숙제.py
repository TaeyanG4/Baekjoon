# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def sol(n):
    arr = []
    for i in range(n):
        s = input().strip()
        numbers = list(map(int, re.findall(r'\d+', s)))
        arr.extend(numbers)
    return sorted(arr)

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    
    # Output
    print(*sol(n))