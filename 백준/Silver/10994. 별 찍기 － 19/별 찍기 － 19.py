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

def sol(n, x, y):
    global star_map
    if n == 1:
        star_map[x][y] = '*'
        return 
    
    length = 4 * n - 3

    for i in range(length):
        star_map[y][x + i] = '*'
        star_map[y + i][x] = '*'
        star_map[y + length - 1][x + i] = '*'
        star_map[y + i][y + length - 1] = '*'
    
    sol(n - 1, x + 2, y + 2)

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = int(input())
    star_map = [[' ' for _ in range(4 * n - 3)] for _ in range(4 * n - 3)]
    
    # output
    sol(n, 0, 0)
    for s in star_map:
        print(''.join(s))