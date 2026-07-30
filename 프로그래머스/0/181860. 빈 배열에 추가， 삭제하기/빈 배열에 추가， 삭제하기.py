def solution(arr, flag):
    answer = []
    for i, f in zip(arr, flag):
        if f:
            answer.extend([i]*i*2)
        else:
            for i in range(i):
                answer.pop()
    return answer