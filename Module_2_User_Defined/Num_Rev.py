def Rev(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
        
    return(rev)

n=int(input("Enter The Number :" ))
print("The Number Is " , n , "And The Reversed Number Is " , Rev(n))