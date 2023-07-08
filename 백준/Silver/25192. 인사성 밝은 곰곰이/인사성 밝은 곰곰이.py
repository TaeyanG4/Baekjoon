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
#################################

def solution(n):
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n = int(input())
    
    # output
    ans = 0
    obj_set = set()
    for i in range(n):
        s = input().rstrip()
        if s == 'ENTER':
            ans += len(obj_set)
            obj_set.clear()
        else:
            obj_set.add(s)
    ans += len(obj_set)
    print(ans)