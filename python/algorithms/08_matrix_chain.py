def chain(P: list[int]) -> int:
    n = len(P)
    m = [[0] * n for _ in P]

    for l in range(2, n):
        for i in range(0, n - l):
            j = i + l - 1
            m[i][j] = min([m[i][k] + m[k + 1][j] + P[i - 1] * P[k] * P[j] for k in range(i, j)])

    return m[0][-2]


assert chain([2, 1, 3, 4]) == 20
assert chain([1, 2, 3, 4, 3]) == 30
assert chain([3, 4]) == 0
assert chain([23, 26, 27, 20]) == 26000
