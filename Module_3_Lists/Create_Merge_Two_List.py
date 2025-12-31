a=[]
b=[]
n=int(input("Enter the number of elements for the first list: "))
for i in range(n):
    num=int(input("Enter a number: "))
    a.append(num)
n=int(input("Enter the number of elements for the second list: "))
for i in range(n):
    num=int(input("Enter a number: "))
    b.append(num)
c=a+b
print("The Merged List Is :",c)