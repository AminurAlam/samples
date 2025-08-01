def binary(array: list[int], query: int) -> bool:
    a, b = 0, len(array) - 1

    while a <= b:
        mid = int((a + b) / 2)
        val = array[mid]

        if query == val:
            return True
        elif query > val:
            a = mid + 1
        elif query < val:
            b = mid - 1

    return False


for test in [
    [],
    [0],
    [1, 2],
    [-1, 1],
    [1, 2, 3],
    [0, 1, 2, 3],
    [1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [0, 2, 4, 6, 8],
    [1, 3, 5, 7, 9],
    [1, 3, 5, 7, 9],
    [2, 5, 8, 11, 14],
]:
    for i in range(-2, 10):
        assert binary(test, i) == (i in test), (test, i)
