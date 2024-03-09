def optimal_bst(keys, freq):
    n = len(keys)

    cost = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            cost[start][end] = float('inf')

            for root in range(start, end + 1):
                left_cost = cost[start][root - 1] if root > start else 0
                right_cost = cost[root + 1][end] if root < end else 0
                total_cost = left_cost + sum(freq[start:root]) + right_cost + sum(freq[root + 1:end + 1])

                if total_cost < cost[start][end]:
                    cost[start][end] = total_cost


    return cost[0][n - 1]


keys = [10, 12, 20]
freq = [34, 8, 50]

result = optimal_bst(keys, freq)
print(f"The minimum cost of constructing an optimal BST is: {result}")
