m=int(input("Enter The Starting Number : "))
n=int(input("Enter The Ending Number : "))
print("The Prime Number From " , m , " Upto" , n , "is")
for num in range (m,n+1):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count +=1
    if count==2:
        print(num , end=" ")
    