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
# from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n):
    ans = 0 
    for i in range(1, n):
        if n % i == 0:
            ans += i
    
    if ans == n:
        print(f'{n} is a perfect number.')
        print()
    elif ans < n:
        print(f'{n} is a deficient number.')
        print()
    else:
        print(f'{n} is an abundant number.')
        print()

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    t = int(input())
    
    # output
    for _ in range(t):
        n = int(input())
        solution(n)