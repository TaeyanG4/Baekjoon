from collections import *
def solution(m, n, h, w, drops):
    INF = len(drops) + 1
    board = [[INF] * n for i in range(m)]
    for t, (r, c) in enumerate(drops, 1):
        board[r][c] = t
        
    # 가로 압축
    row_mi = []
    for i in range(m):
        dq = deque()
        tmp = []
        for j in range(n):
            while dq and dq[0] <= j-w:
                dq.popleft()
            while dq and board[i][dq[-1]] >= board[i][j]:
                dq.pop()
            dq.append(j)
            if j >= w-1:
                tmp.append(board[i][dq[0]])
        row_mi.append(tmp)
    
    # 세로 압축
    area_mi = [[0]*(n-w+1) for i in range(m)]
    for i in range(n-w+1):
        dq = deque()
        for j in range(m):
            while dq and dq[0] <= j-h:
                dq.popleft()
            while dq and row_mi[dq[-1]][i] >= row_mi[j][i]:
                dq.pop()
            dq.append(j)
            if j >= h-1:
                area_mi[j-h+1][i] = row_mi[dq[0]][i]
                
    # 정답 찾기
    mx = max(max(line) for line in area_mi)
    for r in range(m-h+1):
        for c in range(n-w+1):
            if area_mi[r][c] == mx:
                return [r, c]