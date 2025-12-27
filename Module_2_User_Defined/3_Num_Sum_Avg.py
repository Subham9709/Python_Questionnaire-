def Sum_Avg(x,y,z):
    total=x+y+z
    avg=sum/3
    return(total,avg)

a=int(input("Enter The First Number : "))
b=int(input("Enter The Second Number : "))
c=int(input("Enter The Third Number : "))

print("The Sum And Average Is " , Sum_Avg(a,b,c))