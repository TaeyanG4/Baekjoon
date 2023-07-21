# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import time
# import pprint
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(cnt):
    global min_val, max_val, plus, minus, mul, div, calc
    
    if cnt == (n-1):
        temp_val = li[0]
        
        for i in range(n-1):
            if calc[i] == '+':
                temp_val = temp_val + li[i+1]
            elif calc[i] == '-':
                temp_val = temp_val - li[i+1]
            elif calc[i] == '*':
                temp_val = temp_val * li[i+1]
            elif calc[i] == '/':
                temp_val = int(temp_val / li[i+1])
        
        min_val = min(min_val, temp_val)
        max_val = max(max_val, temp_val)
        return
    
    for i in range(4):
        if i == 0 and plus > 0:
            calc.append('+')
            plus -= 1
            solution(cnt+1)
            calc.pop()
            plus += 1
        elif i == 1 and minus > 0:
            calc.append('-')
            minus -= 1
            solution(cnt+1)
            calc.pop()
            minus += 1
        elif i == 2 and mul > 0:
            calc.append('*')
            mul -= 1
            solution(cnt+1)
            calc.pop()
            mul += 1
        else:
            if div > 0:
                calc.append('/')
                div -= 1
                solution(cnt+1)
                calc.pop()
                div += 1
                

if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    li = list(map(int, input().split()))
    plus, minus, mul, div = map(int, input().split())
    calc = []
    min_val = INF
    max_val = -INF
    
    # output
    solution(0)
    print(max_val)
    print(min_val)