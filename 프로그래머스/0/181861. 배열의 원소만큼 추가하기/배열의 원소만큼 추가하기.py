def solution(arr):
    answer = []
    for i in arr:
        answer.extend([i for x in range(i)])
    return answer