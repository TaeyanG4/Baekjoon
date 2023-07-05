def fib(n):
    a, b = 1, 1
    cnt = 0
    for _ in range(n-2):
        a, b = b, a+b
        cnt += 1
    return b, cnt

n = int(input())
print(*fib(n))
