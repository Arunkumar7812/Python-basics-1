num=int(input("Enter the number:"))
pro=1
  
while num>0:
    d=num%10
    pro=pro*d
    num//=10
print(pro)