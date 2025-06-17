### Propagation Of error

x = 2.5
dx = 0.1
y = 3.2
dy = 0.2
n = 3

print(f"addition: z = {x+y} ± {dx + dy}")
print(f"multiplication: z = {x*y} ± {x*y * (dx/x + dy/y)}")
print(f"power: z = {x**y} ± {x**y * (n * dx/x)}")
