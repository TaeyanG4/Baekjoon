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
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    
    # Output
    while True:
        n = int(input())
        cnt = 0
        if n == 0:
            break
        for i in range(n+1):
            cnt += i
        print(cnt)