import sys
input = sys.stdin.readline
import math
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *

def sol(n, l):
    l.sort(key=lambda x: (x[1], x[0]))
    return l

if __name__ == '__main__':
    n = int(input())
    l = [list(map(int ,input().strip().split())) for _ in range(n)]
    sol(n, l)
    for p in l:
        print(p[0], p[1])