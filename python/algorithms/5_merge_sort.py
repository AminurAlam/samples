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


def sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(sort(arr[:mid]), sort(arr[mid:]))


import random

for _ in range(100):
    test = random.sample(range(-10, 20), random.choice(range(1, 10)))
    assert sort(test) == sorted(test), test
