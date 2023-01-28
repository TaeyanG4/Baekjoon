import sys
input = sys.stdin.readline
import math
from collections import deque

def sol(n):
    n = list(set(n))
    n = sorted(n, reverse=True)
    [print(n.pop()) for _ in range(len(n))]

if __name__ == '__main__':
    n = [int(input()) for _ in range(int(input()))]
    sol(n)