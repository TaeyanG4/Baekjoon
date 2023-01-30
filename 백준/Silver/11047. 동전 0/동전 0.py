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

def sol(k, l):
    m = 0
    l.sort(reverse=True)
    for item in l:
        if k - item >= 0 :    
            m += k // item
            k = k % item    
            
        if k == 0 : 
            break  
    return m

if __name__ == '__main__':
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    print(sol(k, l))
