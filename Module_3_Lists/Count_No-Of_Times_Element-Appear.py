a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    num=int(input("Enter a number: "))
    a.append(num)
element_to_count=int(input("Enter the element to count: "))
count=0
for i in a:
    if i==element_to_count:
        count+=1
print("Element",element_to_count,"appears",count,"times.")
