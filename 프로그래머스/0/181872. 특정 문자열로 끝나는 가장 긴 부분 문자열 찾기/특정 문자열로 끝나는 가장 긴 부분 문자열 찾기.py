def solution(myString, pat):
    idx = 0
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            idx = i
    return myString[:idx+len(pat)]