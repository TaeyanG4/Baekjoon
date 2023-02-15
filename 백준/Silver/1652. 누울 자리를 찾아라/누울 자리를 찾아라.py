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

def sol(n, l):
    
    wid_cnt, hei_cnt = 0, 0
    # 가로
    for i in range(n):
        wid = 0
        for j in range(n):
            if l[i][j] == '.':
                wid += 1
            elif l[i][j] == 'X':
                wid = 0
            if wid == 2:
                wid_cnt += 1
    
    # 세로
    for i in range(n):
        hei = 0
        for j in range(n):
            if l[j][i] == '.':
                hei += 1
            elif l[j][i] == 'X':
                hei = 0
            if hei == 2:
                hei_cnt += 1
    return wid_cnt, hei_cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    l = [input().strip() for _ in range(n)]
    
    # Output
    print(*sol(n, l))