### Truncation and Rounding error

print(f"given result: {0.1+0.2}")
print(f"correct result: {round(0.1+0.2, 1)}")

print(f"correct result: {0.123456}")
print(f"given result: {round(0.123456, 2)}")

# # truncatio error example
# x = 0.1
# y = 0.2
# z = x + y
#
# print("actual result:", z)
# print("approx result (truncated):", np.trunc(z))
#
# # rounding error example
# x = 0.123456
# y = round(x, 2)
#
# print("actual result:", x)
# print("approx result (truncated):", y)
