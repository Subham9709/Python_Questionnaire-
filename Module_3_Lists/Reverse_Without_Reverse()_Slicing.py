a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    num=int(input("Enter a number: "))
    a.append(num)
for i in range(len(a)-1,-1,-1):
    print(a[i])
