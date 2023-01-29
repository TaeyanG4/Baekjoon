import sys
import math
import copy
import ast
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *

def sol(command, arr_size, arr):
    
    command = command.replace("RR", "")
    if arr_size == 0:
        arr = deque()
    else:     
        arr = deque(arr)
    
    r_cnt = 0
    for i in command:
        if i == 'R':
            r_cnt += 1
        else:
            if len(arr) < 1:
                return "error"

            if r_cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
    
    if r_cnt % 2 != 0:
        arr.reverse()
        
    return arr

if __name__ == '__main__':
    input = sys.stdin.readline
    
    t = int(input())
    for i in range(t):    
        command = input().strip()
        arr_size = int(input())
        arr = ast.literal_eval(input().strip())
        ans = sol(command, arr_size, arr)
        if ans == "error":
            print(ans)
        else:
            print("[" + ",".join(map(str, ans)) + "]")