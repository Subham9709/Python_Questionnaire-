a = (1, 2, 3, 4, 5)
print("Positive Indexing:")
for i in range(len(a)):
    print("Element at index {}: {}".format(i, a[i]))
print("Negative Indexing:")
for i in range(-1, -len(a)-1, -1):
    print("Element at index {}: {}".format(i, a[i]))
