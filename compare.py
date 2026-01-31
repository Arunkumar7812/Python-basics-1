a=int(input("Enter the first side:"))
b=int(input("Enter the second side:"))
if a+b >a*b:
    print("sum is greater than product")
elif a*b >a+b:
     print("product is greater than sum")
elif a*b == a+b:
    print("Both equals")
    
