#import line
import sys

def solution(li, n):
    memo = [1] * n

    for i in range(n):
        for j in range(i):
            if li[i] > li[j] :
                memo[i] = max(memo[i], memo[j]+1)

    return max(memo)
                
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    li = list(map(int, input().split()))
    
    # output
    print(solution(li, n))
