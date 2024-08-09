import numpy as np

# truncatio error example
x = 0.1
y = 0.2
z = x+y

print("actual result:", z)
print("approx result (truncated):", np.trunc(z))

# rounding error example
x = 0.123456
y = round(x, 2)

print("actual result:", x)
print("approx result (truncated):", y)
