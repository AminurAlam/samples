def linear(arr: list[int], query: int) -> bool:
    for item in arr:
        if item == query:
            return True

    return False


l=lambda a,q:sum(map(lambda x:x==q,a))  # fmt: skip


import random

for _ in range(100):
    test = random.sample(range(-10, 20), random.choice(range(1, 10)))
    for i in range(-2, 10):
        assert linear(test, i) == (i in test), (test, i)
