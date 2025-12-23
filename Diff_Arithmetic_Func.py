n=int(input("Enter The Number = "))

if n<9 :
    print ("The Square OF The Number is" , n**2)

elif n<99:
    a=n//10
    b=n%10
    print ("The Sum Of The Digits Is" , a+b)

elif n<999 :
    a=n//100
    b=(n//10)%10
    c= n%10
    print ("The Product Of The Digits Is " , a*b*c)

else:
    print("The Number IS not Compatible")
    
 