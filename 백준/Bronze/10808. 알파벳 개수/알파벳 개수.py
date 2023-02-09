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

def sol(s):
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('a')] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    s = input().strip()
    
    # Output
    print(*sol(s))

