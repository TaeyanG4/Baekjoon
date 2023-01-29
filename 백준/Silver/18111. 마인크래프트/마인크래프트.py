import sys
import math
import copy
import ast
import re
import statistics as st
from decimal import Decimal
import heapq

def sol(n, m, k, l):
    min_time = 99999999999
    for i in range(257):
        remove_value = 0
        set_value = 0
        
        for x in l:
            for xy in x:
                if xy >= i:
                    remove_value += (xy - i)
                elif xy < i:
                    set_value += (i - xy)
        
        if set_value > remove_value + k:
            continue
        
        if remove_value * 2 + set_value <= min_time:
            min_time = remove_value * 2 + set_value
            height = i
    return min_time, height

if __name__ == '__main__':
    n, m, k = map(int, input().strip().split())
    l = [list(map(int, input().strip().split())) for _ in range(n)]
    print(*sol(n, m, k, l))