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

# 자리수에 따라 증가
def add_digit(digit,num):    
    if digit==1:
        decreasing.append(num)
    else:
        for i in range(num%10):
            add_digit(digit-1,num*10+i)

# 백트래킹
def backtracking(digit):    
    for i in range(digit-1,10):
        add_digit(digit,i)

def sol(n):
    if n>=len(decreasing): #감소하는 숫자가 없을 때
        return -1
    else:
        return decreasing[n]
        
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    
    decreasing=[]
    for i in range(1,11):
        backtracking(i)
        
    # Output
    print(sol(n))
    
# 다른방법
# for i in range(1, 11):
#    for cb in combinations(range(0, 10), i):
#        cb = list(cb)
#        cb.sort(reverse=True)
#        nums.append(int("".join(map(str,cb))))