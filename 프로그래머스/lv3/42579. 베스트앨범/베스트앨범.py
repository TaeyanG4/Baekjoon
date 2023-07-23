from collections import *

def solution(genres, plays):
    ans = []
    dic = defaultdict(list)
    
    for idx, (g, p) in enumerate(zip(genres, plays)):
        dic[g].append((idx, p))
    
    li = sorted(dic.items(), key=lambda x: sum([y[1] for y in x[1]]), reverse=True)
    for g, v in li:
        v.sort(key=lambda x: (-x[1], x[0]))
        ans.extend([x[0] for x in v[:2]])
    
    return ans