def binary(A: list[int], q: int) -> bool:
    a, b = 0, len(A) - 1

    while a <= b:
        mid = (a + b) // 2
        val = A[mid]

        if q == val:
            return True
        elif q > val:
            a = mid + 1
        elif q < val:
            b = mid - 1

    return False


# fmt: off
def b(A,q):
 if len(A)<2:return A==[q]
 m=len(A)//2
 return b(A[m:],q)if q>=A[m]else b(A[:m],q)
# fmt: on


import random

for _ in range(100):
    test = random.sample(range(-10, 20), random.choice(range(1, 10)))
    for i in range(-2, 10):
        assert binary(sorted(test), i) == (i in test), (test, i)
