n=int(input("Enter The Number : "))
print("The Prime Number Upto" , n , "is")
for num in range (2,n+1):
    count=0
    for i in range(1,n+1):
        if num%i==0:
            count +=1
    if count==2:
        print(num , end=" ")
    