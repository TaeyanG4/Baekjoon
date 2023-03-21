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
from pprint import *
#################################

def solution(x, y, n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = int(input())
    paper = [list(map(int,input().split())) for _ in range(n)]
    white, blue = 0, 0
    
    # output
    solution(0, 0, n)
    print(white)
    print(blue)