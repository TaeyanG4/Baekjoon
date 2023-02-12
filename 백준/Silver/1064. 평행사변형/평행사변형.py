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

def length(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def sol(v):
    if (v[3]-v[1])*(v[4]-v[0]) == (v[5]-v[1])*(v[2]-v[0]):
        return -1.0
    else:
        val = []
        val.append(length(v[0],v[1],v[2],v[3]))
        val.append(length(v[2],v[3],v[4],v[5]))
        val.append(length(v[4],v[5],v[0],v[1]))
        val.sort()
        max_val = max(val[0]+val[1], val[1]+val[2], val[2]+val[0])
        min_val = min(val[0]+val[1], val[1]+val[2], val[2]+val[0])
        return (max_val-min_val)*2

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    v = list(map(int, input().split()))
    
    # Output
    print(sol(v))