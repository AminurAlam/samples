def min_max(arr: list[int]) -> tuple[int, int]:
    if len(arr) == 1:
        return arr[0], arr[0]

    mid = len(arr) // 2
    a, A = min_max(arr[:mid])
    b, B = min_max(arr[mid:])

    return a if a < b else b, A if A > B else B


import random

for _ in range(100):
    test = random.sample(range(-10, 20), random.choice(range(1, 10)))
    assert min_max(test) == (min(test), max(test)), test
