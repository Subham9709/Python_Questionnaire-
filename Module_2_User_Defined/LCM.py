def LCM(a,b):
    lcm=max(a,b)
    
    while True:
        if lcm % a == 0 and lcm % b == 0:
         return (lcm)
         break
        lcm+=1
        
a=int(input("Enter The First Number : "))
b=int(input("Enter The First Number : "))
print("The LCM Of " , a , "And" , b  , "is" , LCM(a,b)) 
      
    
