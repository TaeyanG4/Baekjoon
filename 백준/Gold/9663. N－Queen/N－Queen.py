# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

# def put() -> None:
#     for i in range(8):
#         print(f'{pos[i]:2}', end='')
#     print()

def sol(i) -> None:
    global cnt, n
    
    for j in range(n):
        if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + n-1]:
            pos[i] = j
            if i == n-1:
                # put() # 디버깅용
                cnt += 1
            else:
                flag_a[j] = True
                flag_b[i + j] = True
                flag_c[i - j + n-1] = True
                sol(i + 1)
                flag_a[j] = False
                flag_b[i + j] = False
                flag_c[i - j + n-1] = False

if __name__ == '__main__':
    
    # input
    n = int(input())
    pos = [0] * n
    cnt = 0
    flag_a = [False] * n
    flag_b = [False] * (n*2-1)
    flag_c = [False] * (n*2-1)
    
    # output
    sol(0)
    print(cnt)