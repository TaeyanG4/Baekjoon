def solution(arr):
    for i, v in enumerate(arr):
        if v >= 50 and v % 2 == 0:
            arr[i] = arr[i]//2
        elif v < 50 and not v % 2 == 0:
            arr[i] = arr[i]*2
    return arr