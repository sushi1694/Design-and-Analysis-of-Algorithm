INF = float('inf')

def floyds_algorithm(graph):
    n = len(graph)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

graph = [
    [0, INF, INF, INF, 2],
    [3, 0, INF, 1, INF],
    [INF, 7, 0, INF, INF],
    [6, INF, INF, 0, INF],
    [INF, INF, INF, 4, 0]
]

result = floyds_algorithm(graph)

for row in result:
    print(row)
