a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    num=int(input("Enter a number: "))
    a.append(num)
element_to_delete=int(input("Enter the element to delete: "))
if element_to_delete in a:
    del a[a.index(element_to_delete)]
    print("Updated List:",a)
else:
    print("Element not found")
