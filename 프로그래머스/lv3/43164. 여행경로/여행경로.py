from collections import *

def solution(tickets):
    answer = []
    
    dic = defaultdict(list)
    for departure, arrival in tickets:
        dic[departure].append(arrival)
        
    for key in dic.keys():
        dic[key].sort(reverse=True)
    
    stack = ['ICN']
    while stack:
        cur = stack[-1]
        if len(dic[cur]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(dic[cur].pop())
    
    answer.reverse()
    return answer