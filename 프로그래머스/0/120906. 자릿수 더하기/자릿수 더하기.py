def solution(n):
    answer = 0
    while True:
        if n <= 0:
            break
        d, m = n // 10, n % 10
        answer += m
        n = d
    return answer