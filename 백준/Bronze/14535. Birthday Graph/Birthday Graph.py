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
from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
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

    cnt = 0
    while True:
        cnt += 1
        birthday = defaultdict(int)
        n = int(input())
        if n == 0:
            break
        
        for _ in range(n):
            dd, mm , yy = S()
            birthday[mm] += 1
            
        print(f"Case #{cnt}:")
        print(f"Jan:{birthday[1]*'*'}")
        print(f"Feb:{birthday[2]*'*'}")
        print(f"Mar:{birthday[3]*'*'}")
        print(f"Apr:{birthday[4]*'*'}")
        print(f"May:{birthday[5]*'*'}")
        print(f"Jun:{birthday[6]*'*'}")
        print(f"Jul:{birthday[7]*'*'}")
        print(f"Aug:{birthday[8]*'*'}")
        print(f"Sep:{birthday[9]*'*'}")
        print(f"Oct:{birthday[10]*'*'}")
        print(f"Nov:{birthday[11]*'*'}")
        print(f"Dec:{birthday[12]*'*'}")
        