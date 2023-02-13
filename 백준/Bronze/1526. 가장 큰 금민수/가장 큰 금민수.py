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

# case2
def sol(n):
    while True:
        flag = True
        for i in str(n):
            if i!="4" and i!="7":
                flag = False
                n -= 1
        if flag :
            return(n)

# case 1
# def sol(n):
#     for i in range(0, n):
#         if len(str(n-i)) == str(n-i).count('4')+str(n-i).count('7'):
#             return n-i

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    
    # Output
    print(sol(n))