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

    for _ in range(int(input())):
        
        x1, y1, z1 = S()
        x2, y2, z2 = S()
        
        adam = x1 * y2 + y1 * z2 + z1 * x2
        gosia = x2 * y1 + y2 * z1 + z2 * x1
        
        if adam > gosia:
            print("ADAM")
        elif adam < gosia:
            print("GOSIA")
        else:
            print("=")