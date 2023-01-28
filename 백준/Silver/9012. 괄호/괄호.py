import sys
input = sys.stdin.readline
import math
from collections import *
from itertools import *

def sol(l):
    stack = []
    for c in l:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                return 'NO'
            stack.pop()
            
    if not stack:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        l = input()
        print(sol(l))