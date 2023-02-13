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

def sol(n, m):
    if n == 0:
        return 0
    
    w = list(map(int, input().split()))
    
    box_cnt = 0
    stack_book = 0
    for book in w:
        stack_book += book
        if stack_book > m:
            box_cnt += 1
            stack_book = 0
            stack_book += book
    
    return box_cnt + 1

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n, m = map(int, input().split())
    
    # Output
    print(sol(n, m))