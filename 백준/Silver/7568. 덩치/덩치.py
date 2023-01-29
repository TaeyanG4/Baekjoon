import sys
input = sys.stdin.readline
import math
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *

def sol(n, ppl):
    ans = []
    for i in range(n):
        rank = 1
        for j in range(n):
            if i == j:
                continue
            if ppl[i][0] < ppl[j][0] and ppl[i][1] < ppl[j][1]:
                rank += 1
        ans.append(str(rank))
    return ' '.join(ans)

if __name__ == '__main__':
    n = int(input())
    ppl = [list(map(int, input().split())) for _ in range(n)]
    print(sol(n, ppl))