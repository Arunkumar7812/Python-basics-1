a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
max_num=max(a,b)
while True:
    if max_num%a == 0 and max_num%b == 0 :
        lcm=max_num
        break
    max_num+=1
print(lcm)
