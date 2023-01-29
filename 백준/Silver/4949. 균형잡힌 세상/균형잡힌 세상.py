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

def sol(s):
    stack = []
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
                break
        elif c == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)
                break
            
    if not stack:
        return 'yes'
    else:
        return 'no'

if __name__ == '__main__':
    input = sys.stdin.readline
    
    while True:
        s = input()
        if s == '.\n':
            break
        print(sol(s))