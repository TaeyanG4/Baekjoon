def solution(a, d, included):
    answer = 0
    for i, tn in enumerate(included):
        if tn:
            answer += a+i*d
    return answer