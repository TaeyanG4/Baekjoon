## taeyang's template (1.0.8)
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
# from functools import *
#################################


def solution(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if 0 <= ny < r and 0 <= nx < c:
            if not visited[ord(board[ny][nx]) - 65]:
                visited[ord(board[ny][nx]) - 65] = 1
                solution(nx, ny, cnt + 1)
                visited[ord(board[ny][nx]) - 65] = 0


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # input
    r, c = map(int, input().split())
    board = [list(input().strip()) for _ in range(r)]
    visited = [0] * 26
    visited[ord(board[0][0]) - 65] = 1
    ans = 0

    # output
    solution(0, 0, 1)
    print(ans)