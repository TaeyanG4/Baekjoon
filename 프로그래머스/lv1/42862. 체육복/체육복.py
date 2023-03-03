def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i] = -9
            answer += 1
            
    for lostperson in lost:
        if lostperson == -9:
            continue
        if lostperson-1 in reserve:
            reserve.remove(lostperson-1)
            answer += 1
        elif lostperson+1 in reserve:
            reserve.remove(lostperson+1)
            answer += 1
    return answer