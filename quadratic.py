a=int(input("Enter the first side:"))
b=int(input("Enter the second side:"))
c=int(input("Enter the third side:"))
d=b**2 -4*a*c
if d>0:
    print("Real& Distinct")
elif d==0:
    print("Real&equal")
elif d<0:
    print("Imaginary")