def solution(a):
    if 0 < a < 90:
        return 1
    elif a == 90:
        return 2
    elif 90 < a < 180:
        return 3
    elif a == 180:
        return 4