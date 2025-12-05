def bubble(A: list[int]) -> list[int]:
    for i in range(len(A) - 1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]

    return A


import random

for _ in range(100):
    test = random.sample(range(-10, 20), random.choice(range(1, 10)))
    assert bubble(test) == sorted(test), test
