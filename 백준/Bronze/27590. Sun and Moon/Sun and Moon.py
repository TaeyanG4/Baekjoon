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
    
    ds, ys = map(int, input().split())
    dm, ym = map(int, input().split())
    
    for i in range(0, 5000):
        if ds%ys == 0 and dm%ym == 0:
            print(i)
            break
        else:
            ds += 1
            dm += 1