def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        n = int(i[s:s+l])
        if n > k:
            answer.append(n)
    return answer