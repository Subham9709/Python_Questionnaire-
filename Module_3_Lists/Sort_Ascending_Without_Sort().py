a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    num=int(input("Enter a number: "))
    a.append(num)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("Sorted List:",a)
