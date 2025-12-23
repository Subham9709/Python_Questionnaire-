p=int(input("Enter The Priciple Amount = "))
t=int(input("Enter The Time = "))

if p>=100000 :
    r=10

elif p>=75000 :
    r=7.5

elif p>=50000 :
    r=5

elif p>=30000 :
    r=1.5

elif p>=15000 :
    r=0.5

else:
    print ("Number Is Not Compatible")


print("Simple Interest is " , p*r*t/100)
print("Amount is" , (p*r*t)/100 +p )