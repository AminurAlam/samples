def prim(G: list[list[int]]) -> list[str]:
    n = len(G)
    p, k, v = [-1] * n, [int(1e9)] * n, [False] * n

    for _ in range(n):
        x = k.index(min(filter(lambda x: not x[1], zip(k, v)))[0])
        v[x] = True

        for y in range(n):
            if v[y] or not G[x][y] or k[y] <= G[x][y]:
                continue
            k[y] = G[x][y]
            p[y] = x

    return [f"{p[i]}-{i}: {G[p[i]][i]}" for i in range(1, n)]


assert prim(
    [
        [0, 2, 3, 0],
        [2, 0, 1, 1],
        [3, 1, 0, 4],
        [0, 1, 4, 0],
    ]
) == ["0-1: 2", "1-2: 1", "1-3: 1"]

assert prim(
    [
        [0, 19, 8],
        [21, 0, 13],
        [15, 18, 0],
    ]
) == ["2-1: 18", "0-2: 8"]

assert prim(
    [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0],
    ]
) == ["0-1: 2", "1-2: 3", "0-3: 6", "1-4: 5"]
