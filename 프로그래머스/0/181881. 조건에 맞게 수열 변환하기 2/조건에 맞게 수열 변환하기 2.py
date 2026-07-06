def solution(arr):
    answer = 0
    new = []
    while True:
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                new.append(arr[i] // 2)
            elif arr[i] < 50 and arr[i] % 2 == 1:
                new.append(arr[i] * 2 + 1)
            else:
                new.append(arr[i])          
        if new == arr:
            break
        arr = new
        new = []
        answer += 1
    return answer