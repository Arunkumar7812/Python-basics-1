a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
while b!=0:
    a,b = b,a%b
print(a)