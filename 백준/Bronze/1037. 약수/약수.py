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
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    if len(li)%2 == 1:
        print(li[len(li)//2]**2)
    else:
        print(li[0]*li[-1])
