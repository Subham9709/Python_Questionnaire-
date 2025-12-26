def Is_Prime (n):
    flag=0
    for i in range (2,n//2):
        if n % i == 0:
            flag=1
            break
     

    if flag == 0:
        string="The Number Is Prime Xd!!!"
        return(string)    
    
    else:
        string="The Number Is Not Prime Xd!!!"
        return(string)
   
n=int(input("Enter The Number To Be Checked : "))        
print(Is_Prime(n))