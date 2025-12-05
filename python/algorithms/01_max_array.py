def biggest(A: list[int]) -> int:
    result: int = A[0]

    for i in A:
        result = max(result, i)

    return result


b=lambda A:A[0]if len(A)<2 else b(list(map(max,zip(A,A[1:]))))  # fmt: skip


import random

for _ in range(100):
    test = random.sample(range(-10, 20), random.choice(range(1, 10)))
    assert biggest(test) == max(test), (test, b(test))
