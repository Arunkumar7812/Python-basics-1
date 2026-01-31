units=int(input("Enter the number of units purchased: "))

if units<=0:
    print("Invalid number of units.")
elif units<=100:
    bill=0
elif units<=300:
    bill=(units-100)*2
    if bill>200:
        bill=bill+50
elif units>300:
    bill=(200*2)+((units-300)*5)
    bill=bill+100
print(f"Total bill amount: {bill}")