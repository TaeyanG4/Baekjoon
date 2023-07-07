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
from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
# from statistics import *
#################################

def solution(n):
    pass
    
if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(math.factorial(b) // (math.factorial(a) * math.factorial(b-a)))