def solution(num_list):
    tmp1, tmp2 = '', ''
    for v in num_list:
        if v % 2 == 0:
            tmp1 += str(v)
        else:
            tmp2 += str(v)
    return int(tmp1)+int(tmp2)