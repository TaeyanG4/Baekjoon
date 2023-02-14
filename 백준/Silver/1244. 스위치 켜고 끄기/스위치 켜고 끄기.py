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

def sol(switch, student):
    for gender, cnt in student:
        # 남자일 경우
        if gender == 1:
            for i in range(cnt, len(switch)+1, cnt):
                switch[i-1] = 1 if switch[i-1] == 0 else 0
        # 여자일 경우
        if gender == 2:
            switch[cnt-1] = 1 if switch[cnt-1] == 0 else 0
            for i in range(1, min(len(switch)-cnt+1, cnt)):
                if switch[cnt-1-i] == switch[cnt-1+i]:
                    switch[cnt-1-i] = 1 if switch[cnt-1-i] == 0 else 0
                    switch[cnt-1+i] = 1 if switch[cnt-1+i] == 0 else 0
                else:
                    break
    return switch

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    n = int(input())
    switch = list(map(int, input().split()))
    student = [tuple(map(int, input().split())) for _ in range(int(input()))]

    # Output
    ans = sol(switch, student)
    for i in range(0, n, 20):
        print(*ans[i:20+i])