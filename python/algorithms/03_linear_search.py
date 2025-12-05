def linear(A: list[int], q: int) -> bool:
    for item in A:
        if item == q:
            return True

    return False


l=lambda A,q:sum(map(lambda x:x==q,A))  # fmt: skip


import random

for _ in range(100):
    test = random.sample(range(-10, 20), random.choice(range(1, 10)))
    for i in range(-2, 10):
        assert linear(test, i) == (i in test), (test, i)
