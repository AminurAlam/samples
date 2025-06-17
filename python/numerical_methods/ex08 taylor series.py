### taylor's series method

import math

print(f"e¹ = {sum([(1**n)/math.factorial(n) for n in range(100)])}")
print(f"e² = {sum([(2**n)/math.factorial(n) for n in range(100)])}")
print(f"e⁷ = {sum([(5**n)/math.factorial(n) for n in range(100)])}")
