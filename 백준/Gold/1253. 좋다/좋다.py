# import lines
#################################
import sys
# import math
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

# dict를 이용한 방법
# def solution(n, li):
    
#     # 좋은 수의 개수
#     ans = 0
    
#     # 각 숫자가 몇 번 나왔는지 세기
#     dic = defaultdict(int)
#     for i in li:
#         dic[i] += 1
        
#     # 좋은 수 세기
#     for i in range(n):
#         for j in range(i+1, n):
#             temp = li[i] + li[j]
            
#             # 두 수 모두 합한 수와 같을 경우 (0 + 0 = 0)
#             if temp == li[i] and temp == li[j]:
#                 # 3개 이상 나왔을 경우 좋은수를 발견할 수 있다.
#                 if dic[temp] >= 3:
#                     ans += dic[temp]
#                     dic[temp] = 0
                    
#             # 두 수 중 하나만 합한 수와 같을 경우 (0 + 1 = 1)
#             elif temp == li[i] or temp == li[j]:
#                 # 2개 이상 나왔을 경우 좋은수를 발견할 수 있다.
#                 if dic[temp] >= 2:
#                     ans += dic[temp]
#                     dic[temp] = 0
                    
#             # 두 수 모두 합한 수와 다를 경우 (1 + 2 = 3)
#             else:
#                 # 1개 이상 나왔을 경우 좋은수를 발견할 수 있다.
#                 if dic[temp] >= 1:
#                     ans += dic[temp]
#                     dic[temp] = 0
#     return ans

# 투 포인터를 이용한 방법
def solution(n, li):
    ans = 0
    for num in li:
        
        # num을 제외한 temp_li를 만든다.
        temp_li = []
        temp_li.extend(li)
        temp_li.remove(num)
        
        # 맨 왼쪽 temp_li[0], 맨 오른쪽 temp_li[n-2]
        s, e = 0, n-2
        while s < e:
            sum_val = temp_li[s] + temp_li[e]
            if sum_val < num:
                s += 1
            elif sum_val > num:
                e -= 1
            elif sum_val == num: # 좋은 수가 있으면 +1하고 break
                ans += 1
                break
            
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # INF = sys.maxsize
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # input
    n = int(input())
    # li = list(map(int, input().split()))
    li = sorted(map(int, input().split()))

    # output
    print(solution(n, li))