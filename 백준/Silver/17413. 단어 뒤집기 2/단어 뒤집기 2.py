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

def solution(s):
    ans = ''
    
    # input값에 있는 '<'와 '>'를 '_'로 변환후 '_'를 기준으로 split
    s = s.replace('<', '_<').replace('>', '>_').split('_')
    
    # split한 값들을 순회하면서
    for words in s:
        
        # '<'와 '>'가 포함된 값은 그대로 ans에 추가
        # '<'와 '>'가 포함되지 않은 값은 공백을 기준으로 split후 뒤집어서 ans에 추가
        if words.startswith('<'): 
            ans += words
        else:
            ans += ' '.join([word[::-1] for word in words.split()])
            
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    s = input().strip()
    
    # output
    print(''.join(solution(s)))