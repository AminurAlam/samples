def sack(lim: int, n: int) -> int:
    if not (n and lim): return 0

    n -= 1
    return max(sack(lim, n), (val[n] + sack(lim - wht[n], n)) if wht[n] <= lim else 0)


val, wht = [1, 2, 3], [4, 5, 1]
assert sack(3, len(val)) == 3

val, wht = [1, 2, 3], [4, 5, 6]
assert sack(3, len(val)) == 0

val, wht = [300, 200, 400, 500], [2, 1, 5, 3]
assert sack(10, len(val)) == 1200
