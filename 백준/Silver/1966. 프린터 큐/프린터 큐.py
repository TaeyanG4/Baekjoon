from collections import deque
import sys
input = sys.stdin.readline

def sol(n, m, num):
    cnt = 0
    while m >= 0:
        if num[0] == max(num):
            num.popleft()
            cnt += 1
            m -= 1
        else:
            if m == 0:
                num.append(num.popleft())
                m = len(num) - 1
            else:
                num.append(num.popleft())
                m -= 1
    return cnt
        
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        n, m = map(int, input().split())
        num = deque(map(int, input().split()))
        print(sol(n, m, num))