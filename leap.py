year=int(input("Enter te year:"))
if year%400==0:
    print("Leap year")
elif year%4==0 and year%100!=0:
    print("Leap year")
else:
    print("Non leap year")