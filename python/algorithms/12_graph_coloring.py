def safe(lvl: int, c: int) -> int:
    for i in range(len(graph)):
        if graph[lvl][i] and color[i] == c:
            return False
    return True


def graph_col(n_col: int, lvl: int) -> int:
    if lvl == len(graph):
        return 1

    count = 0
    for c in range(1, n_col + 1):
        # if sum([1 for i in range(len(graph)) if graph[vertex][i] and color[i] == c]): continue
        if not safe(lvl, c):
            continue
        color[lvl] = c
        count += graph_col(n_col, lvl + 1)
        color[lvl] = 0
    return count


graph: list[list[int]] = [  #
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
]
color: list[int] = [0] * len(graph)
assert graph_col(3, 0) == 18
