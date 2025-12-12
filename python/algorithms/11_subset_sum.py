def sumsub(col: int, n: int, r: int):
    if col == lim:
        return solutions.append([x[0] for x in zip(wht, sel) if x[1]])
    if n >= len(wht):
        return

    r -= wht[n]
    sel[n] = 1
    if col - r <= lim:
        sumsub(col + wht[n], n + 1, r)
    sel[n] = 0
    if col + r >= lim:
        sumsub(col, n + 1, r)


wht = [1, 9, 7, 5, 18, 12, 20, 15]
sel = [0 for _ in wht]
solutions: list[list[int]] = []
lim = 35

sumsub(0, 0, sum(wht))

for sol in solutions:
    assert sum([x for x in sol]) == lim
assert solutions == [[1, 9, 7, 18], [1, 9, 5, 20], [1, 7, 12, 15], [5, 18, 12], [20, 15]]
assert list(map(lambda x: sum(x), solutions)) == [lim] * len(solutions)
