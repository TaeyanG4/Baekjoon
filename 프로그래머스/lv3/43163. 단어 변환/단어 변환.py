from collections import *

def solution(begin, target, words):
    ans = 0
    if target not in words:
        return ans
    else:
        q = deque()
        q.append((begin, 0))
        while q:
            cur, cnt = q.popleft()
            if cur == target:
                ans = cnt
                break
            for word in words:
                diff = 0
                for i in range(len(word)):
                    if cur[i] != word[i]:
                        diff += 1
                if diff == 1:
                    q.append((word, cnt + 1))
        return ans