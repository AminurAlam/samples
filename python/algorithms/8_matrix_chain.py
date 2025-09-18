import math


def chain(P: list[int]) -> int:
    n = len(P)
    m = [[0 for _ in range(n)] for _ in range(n)]

    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            m[i][j] = 99999
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + P[i - 1] * P[k] * P[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n - 1]


import random

for _ in range(100):
    chain(random.sample(range(1, 20), random.choice(range(2, 10))))
