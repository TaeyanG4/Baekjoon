def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        mx = max(arr)
        flag = False
        for i in range(s, e+1):
            if k < arr[i]:
                mx = min(mx, arr[i])
                flag = True
        if flag:
            answer.append(mx)
        else:
            answer.append(-1)
    return answer