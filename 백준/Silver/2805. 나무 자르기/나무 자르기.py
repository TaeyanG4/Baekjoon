import sys
import math
import copy
import ast
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *

def sol(n, m, l):
    start, end = 0, max(l)
    
    while start <= end:
        mid = (start + end) // 2
        tree = 0
        
        for i in l:
            if i > mid:
                tree += i - mid
                
        if tree >= m:
            start = mid + 1
        else:
            end = mid - 1
    
    return end

if __name__ == '__main__':
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    print(sol(n, m, l))