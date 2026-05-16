def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        v = numLog[i+1] - numLog[i]
        if v == 1:
            answer += 'w'
        elif v == -1:
            answer += 's'
        elif v == 10:
            answer += 'd'
        elif v == -10:
            answer += 'a'
    return answer