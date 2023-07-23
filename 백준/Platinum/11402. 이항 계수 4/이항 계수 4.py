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

# https://husk321.tistory.com/408
# https://mingchin.tistory.com/424

def solution(n, k, m):
    x = 1
    while n * k * x:
        x = x * math.comb(n%m, k%m) % m
        n //= m
        k //= m
    return x

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n, k, m = map(int, input().split())
    
    # output
    print(solution(n, k, m))