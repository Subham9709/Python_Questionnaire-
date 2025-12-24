n=int(input("Enter the Number Of Nummbers To be Entered : "))

# Even Variables
No_of_Even=0
Even_Sum=0
Even_Average=0

# Odd Variables
No_of_Odd=0
Odd_Sum=0
Odd_Average=0

for i in range(n):
    num=int(input("Enter the number : "))
    if num%2==0 :
     Even_Sum+=num
     No_of_Even+=1
    else:
     Odd_Sum+=num
     No_of_Odd+=1
     
Even_Average=Even_Sum/No_of_Even
Odd_Average=Odd_Sum/No_of_Odd

print("The Sum Of Even Numbers And its Average Is" , Even_Sum , " " , Even_Average)
print("The Sum Of Odd Numbers And its Average Is" , Odd_Sum , " " , Odd_Average)

     
     
