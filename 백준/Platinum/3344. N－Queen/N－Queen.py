## taeyang's template (1.0.4)
# https://programming119.tistory.com/172
# https://en.wikipedia.org/wiki/Eight_queens_puzzle
# #3344, #9175, #21133
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

# If the remainder from dividing n by 6 is not 2 or 3 then the list is simply all even numbers followed by all odd numbers not greater than n.
# Otherwise, write separate lists of even and odd numbers (2, 4, 6, 8 – 1, 3, 5, 7).
# If the remainder is 2, swap 1 and 3 in odd list and move 5 to the end (3, 1, 7, 5).
# If the remainder is 3, move 2 to the end of even list and 1,3 to the end of odd list (4, 6, 8, 2 – 5, 7, 9, 1, 3).
# Append odd list to the even list and place queens in the rows given by these numbers, from left to right (a2, b4, c6, d8, e3, f1, g7, h5).

# examples
# 14 queens (remainder 2): 2, 4, 6, 8, 10, 12, 14, 3, 1, 7, 9, 11, 13, 5.
# 15 queens (remainder 3): 4, 6, 8, 10, 12, 14, 2, 5, 7, 9, 11, 13, 15, 1, 3.
# 20 queens (remainder 2): 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 3, 1, 7, 9, 11, 13, 15, 17, 19, 5.

def solution():
    
    # 짝수와 홀수의 별도 리스트를 작성한다
    odd = [*range(1, n + 1, 2)]
    even = [*range(2, n + 1, 2)]

    # n을 6으로 나눈 나머지가 2나 3이 아니면, 리스트는 단순히 n보다 크지 않은 모든 짝수에 이어서 모든 홀수로 구성된다.
    if n % 6 != 2 and n % 6 != 3:
        return even + odd
    
    # 나머지가 2인 경우, 홀수 목록에서 첫번째와 두번째를 교환하고 세번째를 끝으로 옮긴다.
    if n % 6 == 2:
        odd[0], odd[1] = odd[1], odd[0]
        odd.append(odd.pop(2))
        return even + odd
    
    # 나머지가 3인 경우, 홀수 목록에서 첫번째와 두번째를 끝으로 옮기고 짝수 목록에서 첫번째를 끝으로 옮긴다.
    if n % 6 == 3:
        odd.append(odd.pop(0))
        odd.append(odd.pop(0))
        even.append(even.pop(0))
        return even + odd

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    
    # output
    print('\n'.join(map(str, solution())))