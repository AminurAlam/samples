def tsp(G: list[list[int]], mask: int, pos: int) -> int:
    n = len(G)
    if mask == (1 << n) - 1:
        return G[pos][0]

    ans: int = int(1e9)

    for i in range(1, n):
        if mask & (1 << i):
            continue
        ans = min(ans, G[pos][i] + tsp(G, mask | (1 << i), i))

    return ans
    # return min([G[pos][i] + tsp(G, mask | (1 << i), i) for i in range(1, n) if not (mask & (1 << i))])


# fmt: off
assert tsp([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
], 1, 0) == 80

assert tsp([
    [0, 111],
    [112, 0],
], 1, 0,) == 223
