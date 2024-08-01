### FIXED POINT

base = 10

def fixed_point_add(x, y, frac_bits):
    """adds two fixed point numbers"""
    scale = base**frac_bits
    return (x + y) / scale


def fixed_point_mul(x, y, frac_bits):
    """multiplies two fixed point numbers"""
    scale = base**frac_bits
    return (x * y) / (scale * scale)


# example usage
x = 1.25
y = 0.75
frac_bits = 2

result_add = fixed_point_add(int(x * base**frac_bits), int(y * base**frac_bits), frac_bits)
result_mul = fixed_point_mul(int(x * base**frac_bits), int(y * base**frac_bits), frac_bits)

print(result_add)  # 2.0
print(result_mul)  # 0.9375

print(result_add / base**frac_bits)  # 2.0
print(result_mul / base**frac_bits)  # 0.9375


### FLOATING POINT

x = 1.25
y = 0.75
frac_bits = 2

result_add = x + y
result_mul = x * y

print(result_add)  # 2.0
print(result_mul)  # 0.9375
