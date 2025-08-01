def biggest(array: list[int]) -> int:
    if not array:
        raise ValueError

    result: int = array[0]

    for i in array[1:]:
        result = max(result, i)

    return result


for test in [
    [-1],
    [0],
    [1],
    [-1, 0, 1],
    [-1, -1, -1],
    [0, 20, 0],
    [99, 2, 14],
]:
    assert biggest(test) == max(test), test
