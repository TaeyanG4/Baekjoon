# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
from heapq import *
# from itertools import *
# from datetime import datetime
#################################

def solution(s):
    stack = []
    res = ''
    for c in s:
        if c.isalpha():
            res += c
        else:
            if c == '(':
                stack.append(c)
            elif c == '*' or c == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(c)
            elif c == '+' or c == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
    while stack:
        res += stack.pop()
    return res

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    s = list(input().strip())
    
    # output
    print(solution(s))
    