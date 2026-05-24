def solution(x1, x2, x3, x4):
    answer = True
    if (x1 or x2):
        x12 = True
    else:
        x12 = False
    if (x3 or x4):
        x34 = True
    else:
        x34 = False
    if (x12 and x34):
        answer = True
    else:
        answer = False
    return answer