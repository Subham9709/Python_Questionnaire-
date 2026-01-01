a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)
combined = tuple(zip(a, b))
print("Combined Tuple:", combined)
separated = tuple(zip(*combined))
print("Separated Tuples:")
for i, t in enumerate(separated):
    print("Tuple {}: {}".format(i + 1, t))
