def tsp(graph):
    n = len(graph)
    memo = [[-1] * (1 << n) for _ in range(n)]

    def tsp_helper(mask, pos):
        if mask == (1 << n) - 1:
            return graph[pos][0]

        if memo[pos][mask] != -1:
            return memo[pos][mask]

        min_cost = float('inf')
        for next_city in range(n):
            if (mask >> next_city) & 1 == 0:
                cost = graph[pos][next_city] + tsp_helper(mask | (1 << next_city), next_city)
                min_cost = min(min_cost, cost)

        memo[pos][mask] = min_cost
        return min_cost

    return tsp_helper(1, 0)

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

result = tsp(graph)
print(f"The minimum cost of the optimal tour is: {result}")
