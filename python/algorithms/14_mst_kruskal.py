def find(parent: list[int], i: int) -> int:
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def mst(G: list[tuple[int, int, int]]):
    parent: list[int] = list(range(len(G)))
    result: set[tuple[int, int, int]] = set()

    for edges in sorted(G, key=lambda item: item[2]):
        x, y = find(parent, edges[0]), find(parent, edges[1])
        if x == y:
            continue
        parent[max(x, y)] = min(x, y)
        result.add(edges)
    return result


# fmt: off
assert mst([
    (0, 1, 10),
    (0, 2, 16),
    (1, 2, 15),
]) == {(0, 1, 10), (1, 2, 15)}

assert mst([
    (0, 1, 19),
    (0, 2, 8),
    (1, 2, 13),
]) == {(1, 2, 13), (0, 2, 8)}

assert mst([
    (0, 1, 10),
    (0, 2, 5),
    (0, 3, 6),
    (1, 2, 15),
    (2, 3, 4),
]) == {(2, 3, 4), (0, 2, 5), (0, 1, 10)}

assert mst([
    (0, 1, 10),
    (1, 3, 15),
    (2, 3, 4),
    (2, 0, 6),
    (0, 3, 5),
]) == {(2, 3, 4), (0, 3, 5), (0, 1, 10)}

assert mst([
    (0, 1, 2),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 1),
    (2, 3, 4),
]) == {(0, 1, 2), (1, 2, 1), (1, 3, 1)}

assert mst([
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9),
]) == {(0, 1, 2), (1, 2, 3), (0, 3, 6), (1, 4, 5)}

assert mst([
    (1, 3, 5),
    (0, 1, 6),
    (2, 5, 9),
    (5, 4, 10),
    (1, 2, 11),
    (6, 5, 12),
    (0, 6, 15),
    (2, 3, 17),
    (3, 4, 22),
    (2, 6, 25),
]) == {(1, 3, 5), (0, 1, 6), (5, 4, 10), (6, 5, 12), (1, 2, 11), (2, 5, 9)}
