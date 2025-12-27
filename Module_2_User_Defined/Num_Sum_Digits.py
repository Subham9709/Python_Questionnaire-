def Sum_Digits (n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
        
    return(sum)

n=int(input("Enter The Number : "))
print("The Number Is", n , "And The Sum of Its Digits Is" , Sum_Digits(n))