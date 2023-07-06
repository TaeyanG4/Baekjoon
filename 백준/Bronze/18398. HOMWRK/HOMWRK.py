# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
# from statistics import *
#################################

def solution():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    t = int(input())
    for _ in range(t):
        n = int(input())
        for _ in range(n):
            a, b = map(int, input().split())
            print(a+b, a*b)