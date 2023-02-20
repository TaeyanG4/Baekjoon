# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def sol(n, m, command):
    l_stack = list(n)
    r_stack = list()
    
    for c in command:
        if c[0] == 'L':
            if l_stack:
                r_stack.append(l_stack.pop())
        elif c[0] == 'D':
            if r_stack:
                l_stack.append(r_stack.pop())
        elif c[0] == 'B':
            if l_stack:
                l_stack.pop()
        elif c[0] == 'P':
            l_stack.append(c[1])

    return ''.join(l_stack + r_stack[::-1])

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = input().strip()
    m = int(input())
    command = []
    for i in range(m):
        command.append(tuple(map(str, input().split())))
    
    # output
    print(sol(n, m, command))
