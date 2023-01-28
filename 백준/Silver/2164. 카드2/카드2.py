import sys
import math
from collections import deque

def sol(n):
    v = deque([])
    for i in range(n):
        v.append(i+1)
    for i in range(n-1):
        v.popleft()
        v.append(v.popleft())
    return v.pop()

if __name__ == '__main__':
    n = int(input())
    print(sol(n))