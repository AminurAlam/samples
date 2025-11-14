def not_safe(vertex: int, c: int) -> bool:
    for i in range(len(graph)):
        if graph[vertex][i] and color[i] == c:
            return True
    return False


def graph_col(num_colors: int, vertex: int) -> int:
    if vertex == len(graph):
        return 1

    count = 0
    for c in range(1, num_colors + 1):
        if not_safe(vertex, c):
            continue
        color[vertex] = c
        count += graph_col(num_colors, vertex + 1)
        color[vertex] = 0
    return count


graph: list[list[int]] = [  #
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
]
color: list[int] = [0] * len(graph)
assert graph_col(3, 0) == 18
