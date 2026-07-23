def solution(myString):
    return sorted(item for item in myString.split("x") if item)