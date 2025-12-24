n=int(input("Enter the number : "))

i=2
flag=1

if n<=1:
    flag=0
    
else:
    while i<=n//2 :
     if n % i == 0 :
         flag = 0
     i = i+1
    
    
if flag == 1:
    print("The Number Is Prime..")
    
else:
    print("The Number Is Not Prime ....")
        
    
    