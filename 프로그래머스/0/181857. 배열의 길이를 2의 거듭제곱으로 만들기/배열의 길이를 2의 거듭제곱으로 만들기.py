import math
def solution(arr):
    log_arr = math.log(len(arr))
    tmp = 2 ** math.ceil(math.log2(len(arr)))
    arr.extend([0]*(tmp-len(arr)))
    return arr