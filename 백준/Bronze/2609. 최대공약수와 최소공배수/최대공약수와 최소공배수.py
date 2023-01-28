import sys
input = sys.stdin.readline
import math
from collections import deque

def sol(a,b):

    print(math.gcd(a, b))
    print((a*b)//math.gcd(a, b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    sol(a, b)