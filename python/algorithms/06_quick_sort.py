def quick(A: list[int]) -> list[int]:
    if len(A) <= 1:
        return A

    L = [x for x in A[1:] if x < A[0]]
    R = [x for x in A[1:] if x > A[0]]
    return quick(L) + [A[0]] + quick(R)


q=lambda A:A if len(A)<=1 else q([x for x in A[1:]if x<A[0]])+[A[0]]+q([x for x in A[1:]if x>=A[0]])  # fmt: skip

import random

for _ in range(100):
    test = random.sample(range(-10, 20), random.choice(range(1, 10)))
    assert quick(test) == sorted(test), test
