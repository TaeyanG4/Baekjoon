# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import time
# import pprint
# from collections import *
# from heapq import *
# from itertools import *
# from statistics import *
# from datetime import datetime
# from bisect import *
#################################

# https://www.youtube.com/watch?v=k5eqrlPE3RI&t=63s
# https://www.youtube.com/watch?v=3GsBaTqxcjM

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def slope(self, other):
        if self.x == other.x:
            return INF, self.x, self.y
        else:
            return (self.y - other.y) / (self.x - other.x), self.x, self.y
    
    # 2차원 평면에서 벡터의 외적, 양수면 반시계, 음수면 시계, 0이면 평행    
    def cross(self, other):
        return self.x * other.y - self.y * other.x

def ccw(p, a, b):
    return (a - p).cross(b - p) > 0

def solution(li):
    p = min(li)
    idx = li.index(p)
    li[0], li[idx] = li[idx], li[0] # pivot을 맨 앞으로 보냄
    li = li[:1] + sorted(li[1:], key = lambda x: x.slope(p)) # pivot을 제외한 나머지를 기울기 순으로 정렬
    hull = []
    for item in li:
        while len(hull) >= 2 and ccw(hull[-2], hull[-1], item) <= 0:
            hull.pop()
        hull.append(item)
    return len(hull)
if __name__ == '__main__':
    input = sys.stdin.readline
    INF = sys.maxsize
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    li = []
    for _ in range(n):
        a, b = map(int, input().split())
        li.append(Point(a, b))

    # output
    print(solution(li))