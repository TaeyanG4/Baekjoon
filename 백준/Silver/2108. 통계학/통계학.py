import sys
input = sys.stdin.readline
import math
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *

def sol(n, l):
    mean = round(st.mean(l))
    median = round(st.median(l))
    a = sorted(st.multimode(l))
    mode = a[0] if len(a) == 1 else a[1]
    ran = max(l) - min(l)
    return mean, median, mode, ran

if __name__ == '__main__':
    n = int(input())
    l = [int(input()) for _ in range(n)]
    mean, median, mode, ran = sol(n, l)
    print(mean)
    print(median)
    print(mode)
    print(ran)