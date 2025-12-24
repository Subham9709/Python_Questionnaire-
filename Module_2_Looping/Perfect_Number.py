# If I Win , Motu Will Give Me Unlimited Gaming Time
# If I Lose , I Will Give Him 20 Rupees

n=int(input("Enter The Number : "))

sum=0

for i in range (1,n):
    if n%i==0:
        sum = sum + i
        
if sum == n:
    print("The Number Is Perfect...")
    
else:
    print("The Number Is Not Perfect...")
