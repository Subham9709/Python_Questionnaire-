a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    num=int(input("Enter a number: "))
    a.append(num)
sum_a=sum(a)
avg_a=sum_a/n
print(" The Sum Is :",sum_a)
print(" The Average Is :",avg_a)