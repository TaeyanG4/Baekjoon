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

    # input
    n = int(input())
    
    for i in range(n):
        # output
        lst1 = [*map(int, input().split())]
        sm1 = lst1[0]+(lst1[1]*2)+(lst1[2]*3)+(lst1[3]*3)+(lst1[4]*4)+(lst1[5]*10)
        lst2 = [*map(int, input().split())]
        sm2 = lst2[0]+(lst2[1]*2)+(lst2[2]*2)+(lst2[3]*2)+(lst2[4]*3)+(lst2[5]*5)+(lst2[6]*10)
        
        if sm1 > sm2:
            print(f"Battle {i+1}: Good triumphs over Evil")
        elif sm1 < sm2:
            print(f"Battle {i+1}: Evil eradicates all trace of Good")
        else:
            print(f"Battle {i+1}: No victor on this battle field")