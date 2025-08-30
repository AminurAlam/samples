def quick(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    L = [x for x in arr[1:] if x < arr[0]]
    R = [x for x in arr[1:] if x >= arr[0]]
    return quick(L) + [arr[0]] + quick(R)

q=lambda a:a if len(a)<=1 else q([x for x in a[1:]if x<a[0]])+[a[0]]+q([x for x in a[1:]if x>=a[0]])

import random

for _ in range(100):
    test = random.sample(range(-10, 20), random.choice(range(1, 10)))
    assert quick(test) == sorted(test), test
