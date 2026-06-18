def solution(arr):
    first_2, second_2 = -1, -1
    cnt = 0
    for i in range(len(arr)):

        if arr[i] == 2 and cnt == 0:
            first_2 = i
            cnt += 1
        elif arr[i] == 2 and cnt >= 1:
            second_2 = i
            cnt += 1
    if cnt == 0:
        return [-1]
    elif cnt == 1:
        return [2]
    else:
        return arr[first_2:second_2+1]