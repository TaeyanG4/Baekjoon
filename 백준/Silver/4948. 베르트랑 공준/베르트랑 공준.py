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

def sol(n):
    cnt = 0
    eratos = [True] * (2*n+1)
    eratos[0], eratos[1] = False, False
    
    for i in range(2, 2*n+1):
        if eratos[i]:
            for j in range(i*2, 2*n+1, i):
                eratos[j] = False
    
    return eratos[n+1:].count(True)
        
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    
    # Output
    while True:
        n = int(input())
        if n == 0:
            break
        print(sol(n))