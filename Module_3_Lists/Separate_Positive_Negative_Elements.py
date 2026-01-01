a = []

n = 0
while True:
    try:
        n = int(input("Enter the number of elements: "))
        if n < 0:
            print("Please enter a non-negative count.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

for _ in range(n):
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    a.append(num)

# Separate without mutating the list while iterating
positives = [x for x in a if x >= 0]
negatives = [x for x in a if x < 0]

print("Positive Elements:", positives)
print("Negative Elements:", negatives)
