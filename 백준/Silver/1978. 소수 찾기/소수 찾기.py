import sys
import math

def sol(n):
    cnt = 0
    for num in n:
        if num == 1:
            continue
        if num == 2:
            cnt += 1
        else:
            for j in range(2, int(math.sqrt(num)) + 1):
                if num % j == 0:
                    break
            else:
                cnt += 1
    return cnt

if __name__ == '__main__':
    n = [0]*int(input())
    n = list(map(int, input().split()))
    print(sol(n))