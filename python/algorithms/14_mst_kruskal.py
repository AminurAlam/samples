class Graph:
    def __init__(self, graph: list[list[int]]):
        self.V: int = max([x[0] for x in graph] + [x[1] for x in graph])
        self.graph: list[list[int]] = sorted(graph, key=lambda item: item[2])
        self.parent: list[int] = list(range(len(graph)))
        self.rank: list[int] = [1] * len(graph)

    def find(self, parent: list[int], i: int) -> int:
        if parent[i] == i: return i
        return self.find(parent, parent[i])

    def mst(self):
        result: list[list[int]] = []

        for u, v, w in self.graph:
            x, y = self.find(self.parent, u), self.find(self.parent, v)
            if x == y: continue
            result.append([u, v, w])
            uh = self.rank[x] < self.rank[y]
            self.parent[x if uh else y] = y if uh else x
        return set([f"{u}-{v}: {w}" for u, v, w in result])


assert Graph(
    [
        [0, 1, 10],
        [0, 2, 5],
        [0, 3, 6],
        [1, 2, 15],
        [2, 3, 4],
    ]
).mst() == {"2-3: 4", "0-2: 5", "0-1: 10"}

assert Graph(
    [
        [0, 1, 10],
        [1, 3, 15],
        [2, 3, 4],
        [2, 0, 6],
        [0, 3, 5],
    ]
).mst() == {"2-3: 4", "0-3: 5", "0-1: 10"}

assert Graph(
    [
        [0, 1, 2],
        [0, 2, 3],
        [1, 2, 1],
        [1, 3, 1],
        [2, 3, 4],
    ]
).mst() == {"0-1: 2", "1-2: 1", "1-3: 1"}

assert Graph(
    [
        [0, 1, 19],
        [0, 2, 8],
        [1, 2, 13],
    ]
).mst() == {"1-2: 13", "0-2: 8"}

assert Graph(
    [
        [0, 1, 2],
        # [0, 2, 0],
        [0, 3, 6],
        # [0, 4, 0],
        # [1, 0, 2],
        [1, 2, 3],
        [1, 3, 8],
        [1, 4, 5],
        # [2, 0, 0],
        # [2, 1, 3],
        # [2, 3, 0],
        [2, 4, 7],
        # [3, 0, 6],
        # [3, 1, 8],
        # [3, 2, 0],
        [3, 4, 9],
        # [4, 0, 0],
        # [4, 1, 5],
        # [4, 2, 7],
        # [4, 3, 9],
    ]
).mst() == {"0-1: 2", "1-2: 3", "0-3: 6", "1-4: 5"}
