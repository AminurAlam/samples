def safe2(G: list[list[int]], x: int, y: int) -> int:
    for i in range(x):
        if G[i][y]:
            return 0

    i, j = x, y
    while i and j:
        i, j = i - 1, j - 1
        if G[i][j]:
            return 0

    i, j = x, y
    while i and j < n - 1:
        i, j = i - 1, j + 1
        if G[i][j]:
            return 0

    return 1


def taken(x: int, y: int) -> bool:
    i, jl, jr = x, y, y
    while i:
        i, jl, jr = i - 1, jl - 1, jr + 1
        if jl >= 0 and G[i][jl]:
            return True
        if jr < n and G[i][jr]:
            return True
        if G[i][y]:
            return True
    return False


def nqueen(x: int):
    for y in range(n):
        if taken(x, y):
            continue
        G[x][y] = 1
        if x == n - 1:
            result.append([row.index(1) + 1 for row in G])
        nqueen(x + 1)
        G[x][y] = 0


n = 4
G: list[list[int]] = [[0] * n for _ in range(n)]
result: list[list[int]] = []
nqueen(0)

assert result == [[2, 4, 1, 3], [3, 1, 4, 2]]
