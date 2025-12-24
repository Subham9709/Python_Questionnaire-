n=int(input('Enter The Number Of Numbers to be Entered :- '))

total = 0
# average=0

for i in range (n):
    num=int(input("Enter The Number : "))
    total = total + num
    
average=total/n


print("The Sum Of The N Numbers Is : " , total)
print("The Average Of The N numbers Is :" , average  )

    