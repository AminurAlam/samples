### Fixed and Floating Point Arithmetic

x = 1.25
y = 0.75
scale = 10**2

# FIXED POINT
print((x * scale + y * scale) / scale)  # 2.0
print((x * scale * y * scale) / (scale * scale))  # 0.9375

# FLOATING POINT
print(x + y)  # 2.0
print(x * y)  # 0.9375
