def bubble(array: list[int]) -> list[int]:
    for i in range(len(array) - 1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


for test in [
    [],
    [-1],
    [0],
    [1],
    [-1, 0, 1],
    [1, 2, 3],
    [-10, 10, 20, 30],
    [99, 66, 77, 1],
    [99, 0, 0, 0],
    [0, 0, 0, 99],
]:
    assert bubble(test) == sorted(test), test
