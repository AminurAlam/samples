def safe2(grid: list[list[int]], x: int, y: int) -> int:
    for i in range(x):
        if grid[i][y]:
            return 0

    i, j = x, y
    while i and j:
        i, j = i - 1, j - 1
        if grid[i][j]:
            return 0

    i, j = x, y
    while i and j < n - 1:
        i, j = i - 1, j + 1
        if grid[i][j]:
            return 0

    return 1


def taken(x: int, y: int) -> int:
    i, j1, j2 = x, y, y
    while i:
        i, j1, j2 = i - 1, j1 - 1, j2 + 1
        if j1 >= 0 and grid[i][j1]:
            return 1
        if j2 < n and grid[i][j2]:
            return 1
    return sum([grid[i][y] for i in range(x)])


def nqueen(x: int, result: list[list[int]] = []) -> list[list[int]]:
    for y in range(n):
        if taken(x, y):
            continue
        grid[x][y] = 1
        if x == n - 1:
            result.append([row.index(1) + 1 for row in grid])
        nqueen(x + 1)  # pyright: ignore[reportUnusedCallResult]
        grid[x][y] = 0
    return result


n = 4
grid: list[list[int]] = [[0] * n for _ in range(n)]
print(nqueen(0))  # [[2, 4, 1, 3], [3, 1, 4, 2]]
