def solution(n_str):
    cnt = 0
    for c in n_str:
        if c == '0':
            cnt += 1
        else:
            break
    return n_str[cnt:]