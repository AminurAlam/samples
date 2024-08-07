# adds two fixed point numbers
def fixed_point_add(x, y):
    return (x + y) / scale


# multiplies two fixed point numbers
def fixed_point_mul(x, y):
    return (x * y) / (scale * scale)


x = 1.25
y = 0.75
scale = 10**2

# FIXED POINT
result_add = fixed_point_add(x * scale, y * scale)
result_mul = fixed_point_mul(x * scale, y * scale)

print(result_add)  # 2.0
print(result_mul)  # 0.9375

# FLOATING POINT
result_add = x + y
result_mul = x * y

print(result_add)  # 2.0
print(result_mul)  # 0.9375
