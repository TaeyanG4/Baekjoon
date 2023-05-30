#import line
import sys
import heapq
import math
from collections import deque

def solution(n):
    
    dp = [0, 1]
    
    for i in range(2, n+1):
        minval = 1e9
        j = 1
        while j**2 <= i:
            minval = min(minval, dp[i-(j**2)])
            j += 1
        dp.append(minval + 1) 
    return dp[n]

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    
    # output
    print(solution(n))

