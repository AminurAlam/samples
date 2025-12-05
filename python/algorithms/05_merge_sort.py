def merge(L: list[int], R: list[int]) -> list[int]:
    res: list[int] = []
    i = j = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1

    return res + L[i:] + R[j:]


def sort(A: list[int]) -> list[int]:
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    return merge(sort(A[:mid]), sort(A[mid:]))


import random

for _ in range(100):
    test = random.sample(range(-10, 20), random.choice(range(1, 10)))
    assert sort(test) == sorted(test), test
