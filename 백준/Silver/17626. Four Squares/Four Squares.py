#import line
import sys
import heapq
import math
from collections import deque

def solution(n):
    
    if int(math.sqrt(n)) == math.sqrt(n):
        return 1
    
    for i in range(1, int(math.sqrt(n))+1):
        if int(math.sqrt(n-i*i)) == math.sqrt(n-i*i):
            return 2

    for i in range(1, int(math.sqrt(n))+1):
        for j in range(1, int(math.sqrt(n-i*i))+1):
            if int(math.sqrt(n-i*i-j*j)) == math.sqrt(n-i*i-j*j):
                return 3
    
    return 4

if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    
    # output
    print(solution(n))

