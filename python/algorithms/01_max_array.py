def biggest(arr: list[int]) -> int:
    result: int = arr[0]

    for i in arr:
        result = max(result, i)

    return result


b=lambda a:a[0]if len(a)<2 else b(list(map(max,zip(a,a[1:]))))  # fmt: skip


import random

for _ in range(100):
    test = random.sample(range(-10, 20), random.choice(range(1, 10)))
    assert biggest(test) == max(test), (test, b(test))
