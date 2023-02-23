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

def sol(buckets, m):
    for _ in range(m):
        i, j, k = map(int, input().split())
        i, j, k = i-1, j-1, k-1
        buckets = buckets[:i] + buckets[k:j+1] + buckets[i:k] + buckets[j+1:]
    return buckets
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n, m = map(int, input().split())
    buckets = [i for i in range(1, n+1)]
    
    # output
    print(*sol(buckets, m))