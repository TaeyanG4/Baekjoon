# import lines
#################################
import sys
# import math
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

def solution(n):
    ans = n
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            ans -= ans / i
    
    if n > 1:
        ans -= ans / n
    
    return int(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    
    # output
    print(solution(n))