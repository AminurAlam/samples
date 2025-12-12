def prim(G: list[list[int]]) -> list[str]:
    n = len(G)
    parent = [-1] * n
    kv: list[list[int | bool]] = [[int(1e9), False] for _ in G]

    for _ in range(n):
        u = kv.index(min(filter(lambda x: not x[1], kv)))
        kv[u][1] = True

        for v in range(n):
            if kv[v][1] or not G[u][v] or kv[v][0] <= G[u][v]:
                continue
            kv[v][0] = G[u][v]
            parent[v] = u

    return [f"{parent[i]}-{i}: {G[parent[i]][i]}" for i in range(1, n)]


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
