n = int(input("Enter a number: "))

odd_sum = 0
even_sum = 0
pos = 1

while n > 0:
    digit = n % 10
    if pos % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    n = n // 10
    pos += 1

print("Odd position digits sum:", odd_sum)
print("Even position digits sum:", even_sum)