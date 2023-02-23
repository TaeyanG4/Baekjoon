# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import pprint
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def sol(x, y ,n):
    global neg, zero, pos, paper

    checker = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != checker:
                for k in range(3):
                    for l in range(3):
                        sol(x+k*n//3, y+l*n//3, n//3)
                return
    if checker == -1:
        neg += 1
    elif checker == 0:
        zero += 1
    else:
        pos += 1

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    neg, zero, pos = 0, 0, 0
    
    # output
    sol(0, 0, n)
    print(f"{neg}\n{zero}\n{pos}")
    