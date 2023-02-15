# import line
#################################
import sys
#################################
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_non_prime(n):
    if n == 1:
        return 6
    if n == 2:
        return 6
    if n == 3:
        return 6
    n += 1
    while is_prime(n):
        n += 1
        return n
    return n

if __name__ == '__main__':
    input = sys.stdin.readline
    
    n = int(input())
    print(next_non_prime(n))