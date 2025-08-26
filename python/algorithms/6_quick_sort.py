def quick(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    else:
        left = [x for x in arr[1:] if x < arr[0]]
        right = [x for x in arr[1:] if x >= arr[0]]
        return quick(left) + [arr[0]] + quick(right)


for test in [
    [],
    [-1],
    [0],
    [1],
    [18, 6, 4, 9, 8, 9, 8, 10, 1, 8],
    [3, 10, 1, 3, 6, 1, 8, 2, 5, 5],
    [-3, 10, 9, 2, 5, 1, 8, 6, 10, 8],
    [18, 8, 4, 7, 3, 6, 6, 2, 1, 9],
    [9, 4, 8, 5, 9, 10, 3, 3, 2, 4],
    [6, 9, 4, 9, 9, 2, 8, -2, 4, 8],
    [13, 10, 5, 6, 8, 10, 7, 8, 4, 6],
    [5, 5, 10, 2, 4, 1, 3, 3, 6, 4],
    [0, 5, 9, 9, 3, 4, 9, 1, 7, 8],
    [5, 8, 5, 1, 10, 5, 7, 6, 10, 8],
]:
    assert quick(test) == sorted(test), test
