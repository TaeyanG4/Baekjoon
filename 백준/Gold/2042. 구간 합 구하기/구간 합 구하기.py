# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

# https://one10004.tistory.com/242
# https://www.youtube.com/watch?v=1d9sqmuLy-o

# 세그먼트 트리 초기화
# start, end: 범위(구간), node: 세그먼트 트리에서 노드 번호 
def init(node, start, end):
    # start와 end가 같다는 것은 leaf node임을 의미한다.
    if start == end:
        tree[node] = nums[start]
        return

    mid = (start + end) // 2
    init(node*2, start, mid) # 왼쪽 자식 노드의 구간합
    init(node*2 + 1, mid+1, end) # 오른쪽 자식 노드의 구간합 
    
    # 왼쪽 자식 노드에 있는 구간합과 오른쪽 자식 노드에 있는 구간합을 더한 값을 저장
    tree[node] = tree[node*2] + tree[node*2 + 1]

# 세그먼트 트리의 구간합
# node: 현재 노드
# start: 구하고자 하는 구간합의 왼쪽 구간
# end: 구하고자 하는 구간합의 오른쪽 구간
# left: 노드의 왼쪽 구간
# right: 노드의 오른쪽 구간
def seg_sum(node, start, end, left, right):
    # 구하고자 하는 구간합의 구간 안에 현재 노드의 구간이 포함되지 않는다면
    # 0을 반환한다.
    if end < left or right < start:
        return 0

    # 구하고자 하는 구간합의 구간 안에 현재 노드의 구간이 포함된다면
    # 현재 노드의 값을 반환한다.
    if start <= left and right <= end:
        return tree[node]

    # 구간이 겹치는 경우에는 자식 노드에 대하여 sum 함수를 호출한다.
    mid = (left + right) // 2
    return seg_sum(node*2, start, end, left, mid) + seg_sum(node*2 + 1, start, end, mid+1, right)

# 세그먼트 트리 업데이트
# node: 현재 노드
# start: 노드의 왼쪽 구간
# end: 노드의 오른쪽 구간
# idx: 바꿀 값의 인덱스
# val: 바꿀 값
def update(node, start, end, idx, val):
    if start == end == idx: # 단일 구간 업데이트 
        tree[node] = val
        return
    
    # 현재 노드의 구간에 idx가 포함되지 않을 경우
    # 작업 없이 종료 
    if idx < start or end < idx:
        return

    mid = (start + end) // 2
    update(node*2, start, mid, idx, val) # 왼쪽 자식 노드 업데이트
    update(node*2+1, mid+1, end, idx, val) # 오른쪽 자식 노드 업데이트
    tree[node] = tree[node*2] + tree[node*2 + 1]

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n, m, k = map(int, input().split())
    nums = []
    
    # 트리크기 설정
    h = math.ceil(math.log2(n))
    tree_size = 1 << (h + 1)
    tree = [0] * tree_size
    
    for _ in range(n):
        nums.append(int(input()))
    
    init(node = 1, start = 0, end = n-1)
    
    # output
    for _ in range(m+k):
        a, b, c = map(int, input().split())
        
        if a == 1:
            b -= 1
            update(1, 0, n-1, b, c)
        else:
            b -= 1
            c -= 1
            print(seg_sum(1, b, c, 0, n-1))