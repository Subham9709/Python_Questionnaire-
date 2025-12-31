a=[]
b=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    num=int(input("Enter a number: "))
    a.append(num)
for i in a:
    if i<0:
        b.append(i)
        a.remove(i)
print("Positive Elements:",a)
print("Negative Elements:",b)
