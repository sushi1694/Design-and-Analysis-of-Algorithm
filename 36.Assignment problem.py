def solve_assignment_problem(cost_matrix):
    num_agents = len(cost_matrix)
    num_tasks = len(cost_matrix[0])

    assignment = []

    for agent in range(num_agents):
        min_cost = float('inf')
        task_idx = -1

        for task in range(num_tasks):
            if cost_matrix[agent][task] < min_cost:
                min_cost = cost_matrix[agent][task]
                task_idx = task

        assignment.append((agent, task_idx))

    total_cost = sum(cost_matrix[agent][task] for agent, task in assignment)
    return total_cost, assignment

# Example usage
cost_matrix = [
    [4, 2, 8],
    [6, 5, 1],
    [7, 3, 9]
]

total_cost, assignment = solve_assignment_problem(cost_matrix)

print("Optimal Assignment:")
for agent, task in assignment:
    print(f"Task {task + 1} assigned to Agent {agent + 1}")

print(f"Total Cost: {total_cost}")
