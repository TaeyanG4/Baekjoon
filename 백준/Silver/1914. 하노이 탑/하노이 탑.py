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

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    print(2**n-1)
    
        
    # Output
    if n <= 20:
        hanoi(n, 1, 3)