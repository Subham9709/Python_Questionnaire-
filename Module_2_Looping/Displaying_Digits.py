n=int(input("Enter The Number Of Numbers To Be Entered : "))
single_digit_count=0
double_digit_count=0
triple_digit_count=0

for i in range(n):
    num=int(input("Enter The Number : "))
    if num<=0:
     print("Invalid Number") 
    elif num//100!=0:
     triple_digit_count += 1
     double_digit_count += 1
     single_digit_count += 1
    elif num//10!=0:
     double_digit_count += 1
     single_digit_count += 1
    else:
     single_digit_count +=1
     
print("The Number Of Single , Double And Triple Digits is" , single_digit_count , double_digit_count , triple_digit_count)