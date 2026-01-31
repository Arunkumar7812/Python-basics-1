n = int(input("Enter the number: "))

largest = -1
second_largest = -1

while n > 0:
    digit = n % 10

    if digit > largest:
        if digit != largest:
            second_largest = largest
            largest = digit
    elif digit != largest and digit > second_largest:
        second_largest = digit

    n //= 10

if second_largest == -1:
    print(-1)
else:
    print(second_largest)
