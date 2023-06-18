# import lines
#################################
import sys
import math
import copy
# import ast
# import re
# import time
# import json
import pprint
from collections import *
from heapq import *
from itertools import *
# from datetime import datetime
#################################

# https://blog.naver.com/mesutoezil11/222992449561
# https://velog.io/@veonico/%EB%B0%B1%EC%A4%80-14003.-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4-5-python%ED%8C%8C%EC%9D%B4%EC%8D%AC

def binary_search(arr, target):
    low = -1
    high = len(arr)
    
    while low+1 < high:
        mid = (low+high)//2
        if arr[mid] < target:
            low = mid
        else:
            high = mid
    return high

def solution(n, a):
    li = [sys.maxsize*-1]
    li_idx = [(sys.maxsize*-1, 0)] # num, idx
    a = a[::-1] # 스택으로 활용하기 위해 뒤집음
    
    while a:
        num = a.pop()
        
        # num이 li의 마지막 값보다 크면 li에 추가
        if num > li[-1]:
            li_idx.append((num, len(li)))
            li.append(num)
            
        # num이 li의 마지막 값보다 작으면 이분탐색으로 li에 적절한 위치에 추가  
        else:
            idx = binary_search(li, num)
            li[idx] = num
            li_idx.append((num, idx))
    
    ans_len = len(li)-1 # 0번째는 sys.maxsize*-1이므로 제외
    ans = []

    while li_idx and ans_len:
        num, idx = li_idx.pop()
        if idx == ans_len:
            ans.append(num)
            ans_len -= 1
    
    print(len(ans))
    print(*ans[::-1])

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**9)
    
    # input
    n = int(input())
    a = list(map(int, input().split()))
    
    # output
    solution(n, a)