cp=int(input("Enter the cost price:"))
sp=int(input("Enter the selling price:"))
if cp<sp:
    print("PROFIT")
elif sp<cp:
    print("LOSS")
elif sp==cp:
    print("NO PROFIT NO LOSS")