def Palindrome(n):
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
        
    if rev==n:
        str="The number is an Palindrome xd !!"
        return(str)
    
    else:
        str="The number is not an Palindrome xd !!"
        return(str)

n=int(input("Enter The Number : "))
print(Palindrome(n))