from math import gcd
def HCF(x,y):
    GCD=gcd(x,y)
    return(GCD)

x=int(input("Enter The First Number : "))
y=int(input("Enter The Second Number : "))
print("The HCF Of " , x , "And" , y , "is" , HCF(x,y))