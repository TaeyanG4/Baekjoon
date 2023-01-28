import sys
input = sys.stdin.readline

import math
from collections import deque
from itertools import combinations

def sol(n, m, k):
    cards = sorted(k, reverse=True)
    best_combination = None
    best_sum = 0

    for comb in combinations(cards, 3):
        comb_sum = sum(comb)
        
        if comb_sum <= m and comb_sum > best_sum:
            best_combination = comb
            best_sum = comb_sum

    return sum(best_combination)

if __name__ == '__main__':
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    print(sol(n, m, k))