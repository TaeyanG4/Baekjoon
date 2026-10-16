def solution(picture, k):
    answer = []
    for line in picture:
        tmp = []
        for i in line:
            tmp.append(i*k)
        tmp = ''.join(tmp)
        for _ in range(k):
            answer.append(tmp)
    return answer