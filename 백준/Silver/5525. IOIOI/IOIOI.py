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

def sol(n, io, string):
    cnt = 0
    for i in range(len(string)-n*2):
        if io == string[i:i+n*2+1]:
            cnt += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n, s_len = int(input()), int(input())
    string = input().strip()
    io = 'I'
    for i in range(n):
        io += "OI"
    
    # Output
    print(sol(n, io, string))
