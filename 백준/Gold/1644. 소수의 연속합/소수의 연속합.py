#import line
import sys

def sieve_of_eratosthenes(n):
    primes = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if primes[p] is True:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = []
    for p in range(2, n+1):
        if primes[p]:
            prime_numbers.append(p)

    return prime_numbers

def solution(n):
    primes = sieve_of_eratosthenes(n)
    start, end, cnt = 0, 0, 0
    
    while end <= len(primes):
        if sum(primes[start:end]) == n:
            cnt += 1
            end += 1
        elif sum(primes[start:end]) < n:
            end += 1
        else:
            start += 1
            
    return cnt
    
if __name__ == '__main__':
    input = sys.stdin.readline

    # input
    n = int(input())
    
    # output
    print(solution(n))