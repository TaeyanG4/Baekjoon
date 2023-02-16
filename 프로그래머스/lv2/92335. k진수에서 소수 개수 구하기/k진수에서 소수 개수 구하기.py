import random

# 밀러-라빈 소수 판별법
def miller_rabin(n, val=5):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    # n-1 = 2^r * d 형태로 분해
    r, d = 0, n-1
    while d % 2 == 0:
        r += 1
        d //= 2

    # 밀러-라빈 검사
    for _ in range(val):
        a = random.randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                break
        else:
            return False
    return True

def is_prime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    cnt = 0
    num = []

    # n을 k진수로 변환
    while n > 0:
        num.append(n % k)
        n //= k
    
    # 변환된 수를 0을 기준으로 split함
    numbers = ''.join(str(i) for i in list(reversed(num))).split('0')
    numbers = [x for x in numbers if x != '']
    
    # 소수 판별
    if len(numbers) <= 1:
        for sosu in numbers:
            if miller_rabin(int(sosu)):
                    cnt += 1
    else:
        for sosu in numbers:
            if is_prime(int(sosu)):
                    cnt += 1
    return cnt