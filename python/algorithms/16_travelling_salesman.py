def dfs(G: list[list[int]], vis: list[bool], pos: int):
    if sum(vis) == n:
        return G[pos][0]

    cost: int = int(1e9)

    for city in range(1, n):
        if not vis[city]:
            vis[city] = True
            cost = min(cost, G[pos][city] + dfs(G, vis, city))
            vis[city] = False

    return cost


def rec(G: list[list[int]], mask: int, pos: int) -> int:
    if mask == (1 << n) - 1:
        return G[pos][0]

    ans: int = int(1e9)

    for i in range(1, n):
        if (mask & (1 << i)) == 0:
            ans = min(ans, G[pos][i] + rec(G, mask | (1 << i), i))

    return ans

    # return min([G[pos][i] + rec(G, mask | (1 << i), i) for i in range(1, n) if (mask & (1 << i)) == 0])


def tsp(G: list[list[int]]) -> int:
    vis = [False] * n
    vis[0] = True
    assert dfs(G, vis, 0) == rec(G, 1, 0)
    return rec(G, 1, 0)


g = [  #
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]
n = len(g)
assert tsp(g) == 80

g = [  #
    [0, 111],
    [112, 0],
]

n = len(g)
assert tsp(g) == 223
