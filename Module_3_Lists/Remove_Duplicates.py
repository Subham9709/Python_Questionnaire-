a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    num=int(input("Enter a number: "))
    a.append(num)
b=[]
for i in a:
    if i not in b:
        b.append(i)
print("Original List:",a)
print("List After Removing Duplicates:",b)
