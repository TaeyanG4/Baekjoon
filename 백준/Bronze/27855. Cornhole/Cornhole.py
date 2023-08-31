## taeyang's template (1.0.1)
#################################
## my import lines
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
# from datetime import *
# from bisect import *
#################################

def solution(h1, b1, h2, b2):
    t1 = (h1*3)+b1
    t2 = (h2*3)+b2
    if t1 == t2:
        return "NO SCORE"
    elif t1 > t2:
        return f"1 {t1-t2}"
    else:
        return f"2 {t2-t1}"

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    h1, b1 = map(int, input().split())
    h2, b2 = map(int, input().split())
    
    # output
    print(solution(h1, b1, h2, b2))