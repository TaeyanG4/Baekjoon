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

def sol(s):
    
    stack = []
    temp = 1
    ans = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            temp *= 2
            
        elif s[i] == '[':
            stack.append(s[i])
            temp *= 3
            
        elif s[i] == ')':
            if not stack or stack[-1] == '[':
                return 0
            if s[i-1] == '(':
                ans += temp
            stack.pop()
            temp //= 2
            
        elif s[i] == ']':
            if not stack or stack[-1] == '(':
                return 0
            if s[i-1] == '[':
                ans += temp
            stack.pop()
            temp //= 3
    
    if stack:
        return 0
    else:
        return ans
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    s = input().strip()
    
    # Output
    print(sol(s))