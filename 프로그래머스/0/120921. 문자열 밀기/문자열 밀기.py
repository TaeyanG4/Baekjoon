def solution(A, B):
    cnt = 0
    lst_A = list(A)
    while cnt < len(lst_A):
        if ''.join(lst_A) == B:
            return cnt
        lst_A.insert(0, lst_A.pop())
        cnt += 1
    return -1