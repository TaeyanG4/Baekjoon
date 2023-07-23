# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# import statistics as st
# from decimal import *
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
#################################

def solution(s):
    q = deque(s)
    k, y = "KOREA", "YONSEI"
    k_stack, y_stack = list(), list()
    i, j = 0, 0
    
    while True:
        if k_stack == list(k):
            return k
        
        if y_stack == list(y):
            return y
        
        c = q.popleft()
        if c == k[i]:
            i += 1
            k_stack.append(c)

        if c == y[j]:
            j += 1
            y_stack.append(c)
    
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    s = input().strip()
    
    # output
    print(solution(s))



