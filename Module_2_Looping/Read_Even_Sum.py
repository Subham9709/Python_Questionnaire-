n=int(input('Enter the number of numbers to be entered : '))
Even_Sum=0
Odd_Sum=0

#Input
for i in range(n):
    num=int(input("Enter The Number :"))
    if i%2==0:
     Even_Sum = Even_Sum + num
    else:
     Odd_Sum = Odd_Sum + num
     
print("The Sum of Even Series Is" , Even_Sum , "\n" "The Sum Of Odd Series Is", Odd_Sum)
