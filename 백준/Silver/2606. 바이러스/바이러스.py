# import lines
#################################
import sys
import math
import copy
import ast
import re
import time
import json
import pprint
import statistics as st
from decimal import *
from collections import *
from itertools import *
from heapq import *
#################################

def solution(start_node, graph):
    visited = []
    queue = deque([start_node])

    while queue:
        cur_node = queue.popleft()  # 리스트의 queue.pop(0)과 같다. 그러나 시간복잡도 상수시간 보장
        if cur_node not in visited:
            visited.append(cur_node)
            queue.extend(graph[cur_node])
    return len(visited) - 1


if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n = int(input())
    m = int(input())
    dic = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        dic[a].append(b)
        dic[b].append(a)

    # output
    print(solution(1, dic))