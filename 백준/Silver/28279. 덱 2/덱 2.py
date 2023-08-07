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
from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

def solution(n):
    dq = deque()
    for i in range(n):
        cmd = input().split()
        if cmd[0] == '1':
            dq.appendleft(cmd[1])
        elif cmd[0] == '2':
            dq.append(cmd[1])
        elif cmd[0] == '3':
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif cmd[0] == '4':
            if dq:
                print(dq.pop())
            else:
                print(-1)
        elif cmd[0] == '5':
            print(len(dq))
        elif cmd[0] == '6':
            if dq:
                print(0)
            else:
                print(1)
        elif cmd[0] == '7':
            if dq:
                print(dq[0])
            else:
                print(-1)
        elif cmd[0] == '8':
            if dq:
                print(dq[-1])
            else:
                print(-1)

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    
    # output
    solution(n)