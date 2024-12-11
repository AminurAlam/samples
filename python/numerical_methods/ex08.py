### taylor's series method

import math

x0 = 0
x = 1
approx = 1

for n in range(1, 6):
    approx += (math.exp(x0) / math.factorial(n)) * (x - x0) ** n

print(f"e¹ = {approx}")
