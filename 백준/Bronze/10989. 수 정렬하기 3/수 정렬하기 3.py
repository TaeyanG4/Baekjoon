import sys
input = sys.stdin.readline
import math
from collections import *
from itertools import *
from heapq import *

def sol(n, l):
    for i in range(n):
        num = int(input())
        l[num] += 1
    for i in range(10001):
        if l[i] != 0:
            for j in range(l[i]):
                print(i)

if __name__ == '__main__':
    n = int(input())
    l = [0] * 10001
    sol(n, l)

    