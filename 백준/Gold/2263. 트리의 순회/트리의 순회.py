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

def solution(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    parent = postorder[post_end]
    print(parent, end=" ")
    
    left = p[parent] - in_start
    right = in_end - p[parent]
    
    solution(in_start, in_start+left-1, post_start, post_start+left-1)
    solution(in_end-right+1, in_end, post_end-right, post_end-1)
    
if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    
    p = [0] * (n+1)
    for i in range(n):
        p[inorder[i]] = i
    
    # output
    solution(0 ,n-1, 0, n-1)