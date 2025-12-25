n = int(input("Enter a number: "))

last_digit = n % 10

first_digit = n
while first_digit >= 10:
    first_digit = first_digit // 10

sum_digits = first_digit + last_digit
print("Sum of unit digit and last digit:", sum_digits)
