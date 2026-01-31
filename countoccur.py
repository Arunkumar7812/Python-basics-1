n = int(input("Enter the number: "))
d = int(input("Enter the digit to count: "))

count = 0

if n == 0 and d == 0:
    count = 1

while n > 0:
    if n % 10 == d:
        count += 1
    n //= 10

print(count)
