import sys
input = sys.stdin.readline
import math
from collections import *
from itertools import *

def sol(n_arr, m_arr):
    l = Counter(n_arr)
    ans = []
    for i in m_arr:
        ans.append(l[i])

    return ans

if __name__ == '__main__':
    n = int(input())
    n_arr = list(map(int, input().split()))
    m = int(input())
    m_arr = list(map(int, input().split()))
    ans = sol(n_arr, m_arr)
    for i in ans:
        print(i, end=' ')