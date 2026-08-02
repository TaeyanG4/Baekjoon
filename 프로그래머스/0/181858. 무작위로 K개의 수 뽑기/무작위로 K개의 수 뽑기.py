def solution(arr, k):
    answer = []
    while True:
        if len(answer) == k:
            break
        if arr:
            v = arr.pop(0)
            if v not in answer:
                answer.append(v)
        else:
            answer.append(-1)
    return answer