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
from collections import *
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
    dic = defaultdict(bool)
    
    # output
    dic['ChongChong'] = True
    for _ in range(n):
        s1, s2 = input().split()
        if dic[s1] == True or dic[s2] == True:
            dic[s1], dic[s2] = True, True
    print(list(dic.values()).count(True))