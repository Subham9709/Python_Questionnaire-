print("The Armstrong Numbers Upto 500 are :- ")
for num in range (1,501):
    temp = num
    digits = 0

    # count number of digits
    t = num
    while t > 0:
        digits += 1
        t //= 10

    sum = 0
    t = num

    # calculate sum of powers of digits
    while t > 0:
        r = t % 10
        sum += r ** digits
        t //= 10

    if sum == num:
        print(num)
