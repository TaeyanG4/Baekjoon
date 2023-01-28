import sys
input = sys.stdin.readline
import math
from collections import *
from itertools import *

def sol(n, k):
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(sol(n, k))