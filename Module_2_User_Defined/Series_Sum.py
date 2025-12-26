def Series_Sum (n):
    sum=0
    for i in range(n+1):
        sum += i
    
    return sum

n=int(input("Enter The Number Upto Which Series Is Required : "))
print("The Sum Of Series From 1 to N Is :" , Series_Sum(n))
