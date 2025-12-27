def Is_Armstrong (n):
    temp=n
    count=len(str(n))
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**count
        temp=temp//10
        
    temp=n
    if sum==temp:
        string="The Number IS An Armstrong Number Xd!!!"
        return(string)
    
    else:
        string="The Number IS Not An Armstrong Number Xd!!!"
        return(string)
    
n=int(input("Enter The Number : "))
print(Is_Armstrong(n))