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

def sol(sen):
    cnt = 0
    for c in sen:
        if c == 'a' or c == 'A':
            cnt += 1
        elif c == 'e' or c == 'E':
            cnt += 1
        elif c == 'i' or c == 'I':
            cnt += 1
        elif c == 'o' or c == 'O':
            cnt += 1
        elif c == 'u' or c == 'U':
            cnt += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    
    # Output
    while True:
        sen = input().strip()
        if sen == '#':
            break
        print(sol(sen))
    
