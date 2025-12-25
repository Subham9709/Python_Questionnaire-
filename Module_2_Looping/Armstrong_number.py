n=int(input("Enter The Number"))
digit_count=0
sum=0
temp=n

while temp  > 0:
    temp = temp //10
    digit_count+=1
    
temp=n

while temp> 0:
    a=temp%10
    sum=sum+a**digit_count
    temp=temp//10
    
if sum==n:
    print("The Number Is An Armstrong Number....")
    
else:
    print("Not A Armstrong Number")

    