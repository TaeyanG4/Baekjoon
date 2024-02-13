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
    S = lambda: map(float, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    dic = {
        'Wide Receiver' : [4.5, 150, 200],
        'Lineman' : [6.0, 300, 500],
        'Quarterback' : [5.0, 200, 300]
    }
    
    while True:
        a, b, c = S()
        b, c = int(b), int(c)
        if a == b == c == 0:
            break
        flag = False
        for key in dic:
            if dic[key][0] >= a and dic[key][1] <= b and dic[key][2] <= c:
                print(key, end=' ')
                flag = True
        
        if flag == False:
            print('No positions')
        else:
            print()