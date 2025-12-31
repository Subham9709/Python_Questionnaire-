a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    num=int(input("Enter a number: "))
    a.append(num)
even_count=0
odd_count=0
for i in a:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("The Count Of Even Numbers Is :",even_count)
print("The Count Of Odd Numbers Is :",odd_count)
