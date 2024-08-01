import math


def abs_error_add(x, dx, y, dy):
    return dx + dy


def rel_error_mul(x, dx, y, dy):
    return (dx / x) + (dy / y)


def rel_error_pow(x, dx, n):
    return n * (dx / x)


# example usage
x = 2.5
dx = 0.1
y = 3.2
dy = 0.2
n = 3

# add
z_add = x + y
dz_add = abs_error_add(x, dx, y, dy)
print(f"addition: z = {z_add} ± {dz_add}")

# mul
z_mul = x * y
dz_mul = z_mul * rel_error_mul(x, dx, y, dy)
print(f"multiplication: z = {z_mul} ± {dz_mul}")

# power
z_pow = x ** y
dz_pow = z_pow * rel_error_pow(x, dx, n)
print(f"power: z = {z_pow} ± {dz_pow}")
