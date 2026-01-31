num=int(input("Enter the number:"))
e_count=0
o_count=0

if num==0:
    count=1
else:
    num=abs(num)
    while num>0:
        if(num%2==0):
            e_count=e_count+1
        else:
            o_count=o_count+1
        num//=10
print(e_count)
print(o_count)