n=str(input("Enter The String:- "))
rev=""
i=len(n)-1

while i >= 0:
    rev=rev + n[i]
    i -= 1
    
if n ==  rev:
    print("Palindrome Xd!!!")
    
else:
    print("Not A Palindrome Xd!!! 😢😢")