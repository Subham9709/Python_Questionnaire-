n=int(input("Enter The Number Of Numbers To Be Entered : "))
small=9999
large=1

for i in range(n):
    num=int(input("Enter The Number : "))
    if num>9999 or num<1:
        print("Invalid Number Xd!!")
    elif num>large:
        large=num
    elif num<small:
        small=num
    else :
        num=None
        
print("The Greatest Number Is" , large ,'\n The Smallest Number Is' , small)
        