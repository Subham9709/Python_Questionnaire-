n=int(input("Enter The Number Upto Which table Is Required : "))

for i in range(1,n+1):
    print("The Multiplication Table Of " , i , "is" )
    for j in range (1,11):
        print (i , "*" , j  , "=" , i*j)
        print()
  
        
        