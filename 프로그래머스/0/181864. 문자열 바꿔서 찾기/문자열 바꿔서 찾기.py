def solution(myString, pat):
    answer = 0
    myString = myString.replace('A', '_').replace('B', 'A').replace('_', 'B')
    if pat in myString:
        answer = 1
    return answer