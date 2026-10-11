import math
def solution(num, total):
    tmp = (total//num) - (math.ceil(num/2)-1)
    answer = [x for x in range(tmp,tmp+num)]
    return answer