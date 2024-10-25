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

    for i in range(int(input())):
        n, w, e = S()
        ans = 0
        for _ in range(n):
            lww, lwe, lew, lee = S()
            if (lww * w) + (lew * e) > (lwe * w) + (lee * e):
                ans += (lww * w) + (lew * e)
            else:
                ans += (lwe * w) + (lee * e)
        print(f'Data Set {i+1}:')
        print(ans)
        print()