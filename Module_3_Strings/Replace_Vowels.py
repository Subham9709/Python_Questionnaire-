a=str(input("Enter The String:- "))
for i in a :
    if i.lower() in ("aeiou"):
       a=a.replace(i,"*")
    else:
        continue
    
print(a)
            