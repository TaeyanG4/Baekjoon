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

def solution():
    pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    stack = []
    
    # output
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == '1':
            stack.append(int(cmd[1]))
        elif cmd[0] == '2':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif cmd[0] == '3':
            print(len(stack))
        elif cmd[0] == '4':
            if stack:
                print(0)
            else:
                print(1)
        elif cmd[0] == '5':
            if stack:
                print(stack[-1])
            else:
                print(-1)