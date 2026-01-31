angle_1=int(input("Enter the first angle:"))
angle_2=int(input("Enter the second angle:"))
angle_3=int(input("Enter the third angle:"))
sum=angle_1+angle_2+angle_3
if (angle_1 >0 and angle_2>0 and angle_3>0) and sum ==180:
    print("Valid Triangle")
else:
    print("Invalid triangle")
    