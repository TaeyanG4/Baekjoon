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

def convert_to_base(n, k):
    if n == 0:
        return '0'
    
    digits = []
    while n:
        digits.append(int(n % k))
        n //= k

    digits = digits[::-1]
    
    return ''.join(str(digit) for digit in digits)

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    n, k = S()
    conv = convert_to_base(n, k)
    tmp = 0
    if '0' in conv:
        for i in conv.split('0'):
            if i == '':
                continue
            tmp += int(i)
    else:
        tmp = int(conv)
    ans = convert_to_base(tmp, k)
    print(ans)