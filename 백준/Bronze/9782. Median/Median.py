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
    
    # input
    cnt = 1
    while True:
        temp = list(map(int, input().split()))
        if temp[0] == 0:
            break
        else:
            # output
            if temp[0] % 2 == 1:
                print(f'Case {cnt}: {temp[temp[0]//2 + 1]:.1f}')
            else:
                print(f'Case {cnt}: {(temp[temp[0]//2] + temp[temp[0]//2 + 1])/2:.1f}')
        cnt += 1