def prim(graph: list[list[int]]) -> list[str]:
    n = len(graph)
    parent = [-1] * n  # Array to store constructed MST
    visited = [False] * n
    key = [9999] * n  # Key values used to pick minimum weight edge in cut

    for _ in range(n):
        u = key.index(min([x[0] for x in zip(key, visited) if not x[1]]))
        visited[u] = True

        for v in range(n):
            if not graph[u][v] or visited[v] or key[v] <= graph[u][v]: continue
            key[v] = graph[u][v]
            parent[v] = u

    return [f"{parent[i]}-{i}: {graph[parent[i]][i]}" for i in range(1, n)]


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
