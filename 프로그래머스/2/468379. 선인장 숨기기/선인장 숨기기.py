from collections import *
def solution(m, n, h, w, drops):
    INF = len(drops) + 1
    board = [[INF] * n for _ in range(m)]
    for t, (r, c) in enumerate(drops):
        board[r][c] = t + 1

    # 가로 슬라이딩 + 모노토닉덱
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

    # 세로 슬라이딩 + 모노토닉덱
    area_idx = [[0] * (n-w+1) for _ in range(m-h+1)]
    for i in range(n-w+1):
        dq = deque()
        for j in range(m):
            while dq and dq[0] <= j-h:
                dq.popleft()
            while dq and row_mi[dq[-1]][i] >= row_mi[j][i]:
                dq.pop()
            dq.append(j)
            if j >= h-1:
                area_idx[j-h+1][i] = row_mi[dq[0]][i]

    # 정답 찾기
    mx = -1
    ans = [0, 0]
    for i in range(m-h+1):
        for j in range(n-w+1):
            if area_idx[i][j] > mx:
                mx = area_idx[i][j]
                ans = [i, j]

    return ans