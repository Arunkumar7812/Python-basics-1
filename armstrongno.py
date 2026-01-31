
num=int(input("Enter the number:"))
temp=num
sum=0
while temp>0:
    d=temp%10
    sum+=d*d*d
    temp//=10
print(sum)
if sum == num:
    print("Armstrong number")
else:
    print("Not Armstrong number")
        