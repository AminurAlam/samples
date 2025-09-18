def knapsack(lim: int, value: list[int], weight: list[int], n: int, matrix: list[list[int]]):
    if n == 0 or lim == 0:
        return 0

    if matrix[n][lim] != -1:
        return matrix[n][lim]

    pick = 0

    if weight[n - 1] <= lim:
        pick = value[n - 1] + knapsack(lim - weight[n - 1], value, weight, n - 1, matrix)

    notPick = knapsack(lim, value, weight, n - 1, matrix)

    matrix[n][lim] = max(pick, notPick)
    return matrix[n][lim]


lim = 4
n = 3
matrix = [[-1] * (lim + 1) for _ in range(n + 1)]


print(knapsack(4, [1, 2, 3], [4, 5, 1], n, matrix))
