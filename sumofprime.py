n = int(input("Enter the number: "))
sum_prime = 0

while n > 0:
    digit = n % 10
    if digit in (2, 3, 5, 7):
        sum_prime += digit
    n //= 10

print(sum_prime)
