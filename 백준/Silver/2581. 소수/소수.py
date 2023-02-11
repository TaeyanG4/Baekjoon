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

def sol(pl, pr):
    arr = []
    if pr == 1:
        print(-1)
    else:
        for i in range(pl, pr+1):
            if i == 1:
                continue
            if i == 2:
                arr.append(i)
                continue
            if i == 3:
                arr.append(i)
                continue
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    break
                if j+1 == int(math.sqrt(i))+1:
                    arr.append(i)
        if len(arr) == 0:
            print(-1)
        else:
            print(sum(arr))
            print(min(arr))

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    pl, pr = int(input()), int(input())
    
    # Output
    sol(pl, pr)