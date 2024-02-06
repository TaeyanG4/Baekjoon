## taeyang's template (1.0.8)
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
# from functools import *
#################################


def solution():
    pass


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # # input
    # dic = {
    #     "Paper": 57.99,
    #     "Printer": 125.50,
    #     "Planners": 31.25,
    #     "Binders": 22.50,
    #     "Calendar": 10.95,
    #     "Notebooks": 11.20,
    #     "Ink": 66.95,
    # }
    
    # ans = 0
    # while True:
    #     s = input().strip()
    #     if s == "EOI":
    #         break
    #     ans += dic[s]
    
    # # output
    # print(f'${ans:.2f}')
    costs = {
        "Paper" : 57.99, 
        "Printer" : 120.50, 
        "Planners" : 31.25, 
        "Binders" : 22.50, 
        "Calendar" : 10.95, 
        "Notebooks" : 11.20, 
        "Ink" : 66.95}
    total = 0
    while True :
        s = input().strip()
        if s == "EOI" : break
        total += costs[s]
        
    print("${:.2f}".format(total))