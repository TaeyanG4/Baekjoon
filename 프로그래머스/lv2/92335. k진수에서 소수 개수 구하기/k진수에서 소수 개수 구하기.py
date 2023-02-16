def solution(n, k):
    cnt = 0
    num = []

    # n을 k진수로 변환
    while n > 0:
        num.append(n % k)
        n //= k
    
    # 변환된 수를 0을 기준으로 split함
    numbers = ''.join(str(i) for i in list(reversed(num))).split('0')
    
    # 소수 판별
    for sosu in numbers:
        if sosu != ''and is_prime(int(sosu)):
                cnt += 1

    return cnt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True