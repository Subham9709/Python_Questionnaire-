for num in range (100,201,5):
    print("The Number Is : " ,  num)
    sum=0
    while num>0:
        a=num%10
        sum +=a
        num=num//10
        
    print("The Sum Of The Digit Of Number Is" , sum )

    