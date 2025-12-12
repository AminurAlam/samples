def apsp(G: list[list[int]]):
    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    return G


I = int(1e9)

# fmt: off
assert apsp([
    [0, 4, I, 5, I],
    [I, 0, 1, I, 6],
    [2, I, 0, 3, I],
    [I, I, 1, 0, 2],
    [1, I, I, 4, 0],
]) == [
    [0, 4, 5, 5, 7],
    [3, 0, 1, 4, 6],
    [2, 6, 0, 3, 5],
    [3, 7, 1, 0, 2],
    [1, 5, 5, 4, 0],
]


assert apsp([
    [0, 5, I, 10],
    [I, 0, 3, I],
    [I, I, 0, 1],
    [I, I, I, 0],
]) == [
    [0, 5, 8, 9],
    [I, 0, 3, 4],
    [I, I, 0, 1],
    [I, I, I, 0],
]
