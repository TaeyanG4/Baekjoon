import sys
input = sys.stdin.readline
import math
from collections import *
from itertools import *

def sol(k, n):
    v = [i for i in range(0, n+1)]
    for i in range(k):
        for j in range(1, n+1):
            if j == n and i == k-1:
                return v[j] + v[j-1]
            else:
                v[j] += v[j-1]
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        k, n = [int(input()) for _ in range(2)]
        print(sol(k, n))
