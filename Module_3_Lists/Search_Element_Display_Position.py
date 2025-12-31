a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    num=int(input("Enter a number: "))
    a.append(num)
search_element=int(input("Enter the element to search: "))
if search_element in a:
    print("Element found at position:", a.index(search_element))
else:
    print("Element not found")
