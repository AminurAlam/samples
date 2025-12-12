def safe(lvl: int, c: int) -> bool:
    for i in range(len(G)):
        if G[lvl][i] and colors[i] == c:
            return False
    return True


def graph_col(lvl: int):
    if lvl == len(G):
        print(colors)
        return

    for c in range(1, n_col + 1):
        if sum([G[lvl][i] and colors[i] == c for i in range(len(G))]):
            continue
        colors[lvl] = c
        graph_col(lvl + 1)
        colors[lvl] = 0


G: list[list[int]] = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
]

colors: list[int] = [0] * len(G)
n_col: int = 2
graph_col(0)
