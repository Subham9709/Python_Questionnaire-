def Sum_Digits_Single (n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
    
    sum_=0
    digit=0
    
    if sum>9:
        temp=sum
        while temp>0:
            digit=temp%10
            sum_+=digit
            temp=temp//10
        sum=sum_
        return(sum) 
    
n=int(input("Enter The Number : "))
print("The Sum Of The Digits Is " , Sum_Digits_Single(n))
