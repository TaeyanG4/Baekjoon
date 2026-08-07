def solution(rank, attendance):
    answer = 0
    d = 10000
    cnt = 0
    for i in range(1, len(rank)+1):
        idx = rank.index(i)
        if cnt >= 3:
            break
        if attendance[idx]:
            answer += idx*d
            d //= 100
    return answer