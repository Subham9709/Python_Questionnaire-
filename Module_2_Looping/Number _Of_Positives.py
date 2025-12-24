n=int(input('Enter the number of numbers to be added : '))
no_of_pos=0
no_of_neg=0
no_of_zeroes=0

# input
for i in range(n):
 num=int(input("Enter the Number :"))
 if num > 0:
     no_of_pos+=1
 elif num < 0:
     no_of_neg+=1
 else:
     no_of_zeroes+=1
    
print("The Number Of Positives , Negatives And Zeroes Respectively Are" ,no_of_pos , "" , no_of_neg , "" , no_of_zeroes)