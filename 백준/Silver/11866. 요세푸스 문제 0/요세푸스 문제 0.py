import sys
input = sys.stdin.readline
import math
from collections import *
from itertools import *

def sol(n, k):
    ans = []
    q = deque([i for i in range(1, n+1)])
    
    for i in range(n):
        for j in range(k-1):
            q.append(q.popleft())
        ans.append(q.popleft())
    return ans

if __name__ == '__main__':
    n, k = map(int, input().split())
    
    ans = sol(n, k)
    print("<" + ", ".join(map(str, ans)) + ">")