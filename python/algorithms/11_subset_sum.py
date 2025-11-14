def sumsub(collection: int, n: int, r: int):
    if collection == target:
        return solutions.append([w for i, w in enumerate(wht) if sel[i]])
    if n >= len(wht):
        return

    r -= wht[n]
    sel[n] = 1
    if collection - r <= target:
        sumsub(collection + wht[n], n + 1, r)
    sel[n] = 0
    if collection + r >= target:
        sumsub(collection, n + 1, r)


wht = [1, 9, 7, 5, 18, 12, 20, 15]
sel = [0 for _ in wht]
solutions: list[list[int]] = []
target = 35

sumsub(0, 0, sum(wht))

print(list(map(lambda x: sum(x), solutions)))
assert solutions == [[1, 9, 7, 18], [1, 9, 5, 20], [1, 7, 12, 15], [5, 18, 12], [20, 15]]
assert list(map(lambda x: sum(x), solutions)) == [target] * len(solutions)
