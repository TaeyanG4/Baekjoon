import sys
input = sys.stdin.readline

def sol(n, b):
    ans = abs(n-100)
    for i in range(1000001):
        flag = True
        for j in str(i):
            if int(j) not in b:
                flag = False
                break
        if flag:
            ans = min(ans, len(str(i))+abs(n-i))
    return ans

if __name__ == '__main__':
    n, m = [int(input()) for _ in range(2)]
    b = [0,1,2,3,4,5,6,7,8,9]
    if m == 0:
        pass
    else:
        temp = list(map(int, input().split()))
        for i in temp:
            b.remove(i)
    print(sol(n, b))