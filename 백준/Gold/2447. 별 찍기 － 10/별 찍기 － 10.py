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
    if n == 1:
        return '*'
    
    stars = solution(n//3)
    li = []
    
    for star in stars:
        li.append(star*3)
    for star in stars:
        li.append(star+' '*(n//3)+star)
    for star in stars:
        li.append(star*3)
    
    return li

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n = int(input())
    
    # output
    print('\n'.join(solution(n)))