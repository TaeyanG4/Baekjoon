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

def sol(li):
    temp = sorted(list(set(li)))
    dic = {temp[i]:i for i in range(len(temp))}
    ans = list(map(lambda x: dic[x], li))
    return ans
    
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    li = list(map(int, input().split()))
        
    # Output
    print(*sol(li))