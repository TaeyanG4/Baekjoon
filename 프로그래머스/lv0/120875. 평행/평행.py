def get_slope(a, b):
    if a[0] == b[0] or a[1] == b[1]:
        return 0
    return (a[0]-b[0]) / (a[1]-b[1])

def solution(dots):
    if get_slope(dots[0], dots[1]) == get_slope(dots[2], dots[3]) != 0:
        return 1
    if get_slope(dots[1], dots[2]) == get_slope(dots[3], dots[0]) != 0:
        return 1
    if get_slope(dots[0], dots[2]) == get_slope(dots[1], dots[3]) != 0:
        return 1
    return 0