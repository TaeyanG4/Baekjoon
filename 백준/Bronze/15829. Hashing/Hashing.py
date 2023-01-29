import sys
input = sys.stdin.readline
import math
from collections import *
from itertools import *
from heapq import *

def sol(l, s):
    cnt = 0
    for i in range(l):
        cnt += (ord(s[i])-96) * (31**i)
    if cnt > 1234567891:
        return cnt & 1234567891
    else:
        return cnt

if __name__ == '__main__':
    l = int(input())
    s = input()
    print(sol(l, s))