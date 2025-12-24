n=int(input("Enter The Number = "))
sum=0
# Odd Series
print("The Odd Series Is :-")
for i in range(1,n,2):
    sum = sum + i
    print(i,"",end="")

print("\n")
print("The Sum Of The Odd Series Is" , sum)

sum=0
print("\n")

# Even Series
print("The Even series Is :-")
for i in range(0,n,2):
    sum = sum + i
    print(i,"",end="")
    
print("\n")
print("The Sum of Even Series Is :-" , sum) 