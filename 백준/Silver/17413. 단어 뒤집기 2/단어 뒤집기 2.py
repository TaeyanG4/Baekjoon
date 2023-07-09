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
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def solution(s):
    
    stack, ans = [], []
    flag = False
    
    for c in s:
        
        if c == '<':
            flag = True
            while stack:
                    ans.append(stack.pop())
            ans.append(c)
            continue
        elif c == '>':
            flag = False
            ans.append(c)
            continue
        
        if flag:
            ans.append(c)
        else:
            if c == ' ' or c == '<':
                while stack:
                    ans.append(stack.pop())
                ans.append(' ')
            else:
                stack.append(c)
                
    while stack:
                ans.append(stack.pop())
                
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    s = input().strip()
    
    # output
    print(''.join(solution(s)))
