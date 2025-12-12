def sack(lim: int, n: int) -> int:
    if not (n and lim):
        return 0

    n -= 1
    take = 0
    if vw[n][1] <= lim:
        take = vw[n][0] + sack(lim - vw[n][1], n)
    return max(take, sack(lim, n))


vw = [(1, 4), (2, 5), (3, 1)]
assert sack(3, len(vw)) == 3

vw = [(1, 4), (2, 5), (3, 6)]
assert sack(3, len(vw)) == 0

vw = [(300, 2), (200, 1), (400, 5), (500, 3)]
assert sack(10, len(vw)) == 1200
