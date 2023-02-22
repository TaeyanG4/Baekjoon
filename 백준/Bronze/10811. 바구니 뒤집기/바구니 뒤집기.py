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
    ans = [i for i in range(1, n+1)]
    for _ in range(m):
        i, j = map(int, input().split())
        ans[i-1:j] = ans[i-1:j][::-1]
    return ans
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n, m = map(int, input().split())
    
    # output
    print(*sol(n, m))
