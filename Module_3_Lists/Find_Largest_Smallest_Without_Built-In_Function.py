a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    num=int(input("Enter a number: "))
    a.append(num)
largest=a[0]
smallest=a[0]
for i in a:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print("The Largest Is :",largest)
print("The Smallest Is :",smallest)
