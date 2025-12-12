def sumsub(n: int):
    col = sum([x[0] for x in zip(wht, sel) if x[1]])

    if col == lim:
        solutions.append([x[0] for x in zip(wht, sel) if x[1]])
        return
    if col > lim or n >= len(wht):
        return

    sel[n] = 1
    sumsub(n + 1)
    sel[n] = 0
    sumsub(n + 1)


wht = [1, 9, 7, 5, 18, 12, 20, 15]
sel = [0 for _ in wht]
lim = 35
solutions: list[list[int]] = []

sumsub(0)

assert solutions == [
    [1, 9, 7, 18],
    [1, 9, 5, 20],
    [1, 7, 12, 15],
    [5, 18, 12],
    [20, 15],
]
