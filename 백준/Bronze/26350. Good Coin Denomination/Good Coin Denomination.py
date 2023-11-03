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
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    t = int(input())
    
    for _ in range(t):
        flag = True
        n, *lst = S()
        for i in range(n-1):
            if lst[i]*2 > lst[i+1]:
                flag = False
                break
    
        # output
        formatted_list = ' '.join(map(str, lst))
        print(f'Denominations: {formatted_list}')
        if flag:
            print(f'Good coin denominations!')
        else:
            print(f'Bad coin denominations!')
        print()