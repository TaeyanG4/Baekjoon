def solution(n):
    answer = [[0] * n for _ in range(n)] 
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    y, x, cnt = 0, 0, 1

    for _ in range(n**2):
        answer[y][x] = cnt
        cnt += 1
        ny, nx = y + direction[0][0], x + direction[0][1]
        
        if 0 <= ny < n and 0 <= nx < n and not answer[ny][nx]:
            y, x = ny, nx
        else:
            direction.append(direction.pop(0))
            y, x = y + direction[0][0], x + direction[0][1]
    return answer