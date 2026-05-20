def solution(l, r):
    answer = []
    for i in range(l, r+1):
        n = i
        flag = True
        while n > 0:
            n, r = divmod(n, 10)
            if r == 0 or r == 5:
                continue
            else:
                flag = False
                break
        if flag:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer