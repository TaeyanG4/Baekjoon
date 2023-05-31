import sys
import math

def solution(M, N, x, y):
    temp = x
    while temp <= math.lcm(M, N):
        if (temp - y) % N == 0:
            return temp
        temp += M
    return -1
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    t = int(input())
    for _ in range(t):
        M, N, x, y = map(int, input().split())
        # output
        print(solution(M, N, x, y))