# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def sol(n, m):
    ans = [0] * (n)
    for _ in range(m):
        i, j, k = map(int, input().split())
        for p in range(i, j+1):
            ans[p-1] = k
    return ans
    

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n, m = map(int, input().split())
    
    # output
    print(*sol(n, m))