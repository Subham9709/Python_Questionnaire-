n=str(input("Enter The String:- ")).lower()
vowel_count=0
consonant_count=0
for i in n:
    if i.isalpha():
        if i in "aeiou":
            vowel_count=1
        else:
            consonant_count+=1
            
print("The Number Of Vowels Is" , vowel_count)
print("The Number Of Consonants Is" , consonant_count)
