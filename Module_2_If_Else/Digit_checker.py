n=int(input("Enter the Number = "))

n=abs(n)

if n<9 :
    print("Number Is Single Digit")

elif n<99 :
    print("Number Is Double Digit ")

elif n<999 :
    print("Number Is Triple Digit")

elif n<9999 :
    print("Number Is Of 4 Digits")

else :
    print("Number Is Of More Than 4 digits ")