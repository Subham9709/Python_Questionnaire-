from math import factorial

def Factorial (n):
    fact=1
    for i in range (1,n+1):
       fact*=i 
       
    return (fact) 

n=int(input("Enter The Number : "))
print("The Number is" , n , "and the Factorial is" , Factorial(n)) 
