# import lines
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

def sol(x1, y1, x2, y2, x3, y3):
    x_ans, y_ans = 0, 0
    
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    
    for i in range(3):
        if x.count(x[i]) == 1:
            x_ans = x[i]
        if y.count(y[i]) == 1:
            y_ans = y[i]
            
    return x_ans, y_ans

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    
    # Output
    print(*sol(x1, y1, x2, y2, x3, y3))