## taeyang's template (1.0.7)
# https://www.acmicpc.net/problem/11758
# https://burningfalls.github.io/algorithm/boj-25308/
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
from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

# # p1, p2, p3가 반시계 방향이면 양수, 시계 방향이면 음수, 일직선이면 0
# def ccw(p1, p2, p3):
#     return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    
# def save_nodes(lst):
#     nodes = []
#     nodes.append([0, lst[0]])
#     nodes.append([lst[1]/(2 ** 0.5), lst[1]/(2 ** 0.5)])
#     nodes.append([lst[2], 0])
#     nodes.append([lst[3]/(2 ** 0.5), -lst[3]/(2 ** 0.5)])
#     nodes.append([0, -lst[4]])
#     nodes.append([-lst[5]/(2 ** 0.5), -lst[5]/(2 ** 0.5)])
#     nodes.append([-lst[6], 0])
#     nodes.append([-lst[7]/(2 ** 0.5), lst[7]/(2 ** 0.5)])
#     nodes.append([0, lst[0]])
#     nodes.append([lst[1]/(2 ** 0.5), lst[1]/(2 ** 0.5)])
#     return nodes

def solution(a, b, c):
    if a*c * math.sqrt(2) <= b * (a+c):
        return True
    else:
        return False

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    lst = [*S()]
    ans = 0
    
    for nodes in permutations(lst, 8):
        for i in range(8):
            if not solution(nodes[i-2], nodes[i-1], nodes[i]):
                break
        else:
            ans += 1
            
    # output
    print(ans)