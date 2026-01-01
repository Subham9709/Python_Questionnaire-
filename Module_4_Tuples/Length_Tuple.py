a=()
n=int(input("Enter the number of elements of the tuple"))
for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    a += (element,)
print("The length of the tuple is:", len(a))