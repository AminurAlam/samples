def linear(array: list[int], query: int) -> bool:
    for item in array:
        if item == query:
            return True

    return False


for test in [
    [-1, 0, 1],
    [1, 2, 3],
    [1, 3, 5, 7],
    [0, 2, 4, 6],
    [9, 6, 8, 3, 9, 4, 1]
]:
    for i in range(-2, 10):
        assert linear(test, i) == (i in test), test
