a=()
n=int(input("Enter the number of elements of the tuple: "))
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    a += (element,)
print("The maximum element in the tuple is:", max(a))
print("The minimum element in the tuple is:", min(a))
