import sys
input = sys.stdin.readline
import math
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *

def sol(n):
    ans = []
    for _ in range(n):
        v = int(input().strip())
        if v == 0:
            ans.pop()
        else:
            ans.append(v)
    return sum(ans)

if __name__ == '__main__':
    n = int(input())
    print(sol(n))