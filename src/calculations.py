from pulp import LpProblem, LpVariable, LpBinary, lpSum, LpStatus

def calculate_cross_sums(row_targets, col_targets, row_weights, col_weights):
    problem = LpProblem("Binary_Constraint_Solver")

    grid_size = len(row_targets)

    variables = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in range (grid_size)] for i in range(grid_size)]

    for i in range(grid_size):
        problem += lpSum(variables[i][j] * row_weights[i][j] for j in range (grid_size)) == row_targets[i]

    for j in range(grid_size):
        problem += lpSum(variables[i][j] * col_weights[j][i] for i in range (grid_size)) == col_targets[j]

    problem.solve()

    if LpStatus[problem.status] == "Optimal":
        return [[int(variables[i][j].value()) for j in range(grid_size)]    for i in range(grid_size)]
    else:
        print("No solution found.")
        raise Exception("Solution not found")


if __name__ == "__main__":
    row_targets = [3, 13, 14, 11, 10, 17, 1, 5]
    col_targets = [12, 14, 6, 5, 6, 16, 10, 5]

    row_weights = [
        [1, 8, 1, 1, 3, 1, 5, 6],
        [1, 1, 1, 1, 2, 6, 3, 4],
        [2, 7, 3, 8, 2, 8, 2, 1],
        [6, 9, 1, 1, 1, 7, 4, 8],
        [1, 5, 5, 9, 2, 8, 8, 5],
        [8, 8, 2, 6, 2, 2, 1, 4],
        [7, 9, 8, 9, 2, 1, 3, 3],
        [6, 1, 5, 4, 1, 4, 6, 3],
    ]

    col_weights = [
        [1, 1, 2, 6, 1, 8, 7, 6],
        [8, 1, 7, 9, 5, 8, 9, 1],
        [1, 1, 3, 1, 5, 2, 8, 5],
        [1, 1, 8, 1, 9, 6, 9, 4],
        [3, 2, 2, 1, 2, 2, 2, 1],
        [1, 6, 8, 7, 8, 2, 1, 4],
        [5, 3, 2, 4, 8, 1, 3, 6],
        [6, 4, 1, 8, 5, 4, 3, 3],
    ]

    solution = calculate_cross_sums(row_targets, col_targets, row_weights, col_weights)

    print("Solution:")
    for row in solution:
        print(row)