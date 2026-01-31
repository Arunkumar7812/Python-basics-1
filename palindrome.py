num=int(input("Enter the number:"))
a=str(num)
if a == a[::-1]:
    print("palindrome")
else:
    print("Not palindrome")