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
    li = list(map(int, input().split()))
    dp_up, dp_down = [1], [1]
    
    # output
    for i in range(1, len(li)):
        if li[i] >= li[i-1]:
            dp_up.append(dp_up[i-1]+1)
        else:
            dp_up.append(1)
        
        if li[i] <= li[i-1]:
            dp_down.append(dp_down[i-1]+1)
        else:
            dp_down.append(1)
    
    print(max(max(dp_up), max(dp_down)))