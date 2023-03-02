INF = 1e9  # 무한대로 설정합니다.

def solution(n, s, a, b, fares):
    # 플로이드-와샬 알고리즘을 사용하여 최단 거리를 구합니다.
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0
    for fare in fares:
        start, end, cost = fare
        graph[start][end] = cost
        graph[end][start] = cost
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 두 사람이 각각 출발하는 경우와 함께 합승하는 경우를 고려하여 최소 요금을 계산합니다.
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer