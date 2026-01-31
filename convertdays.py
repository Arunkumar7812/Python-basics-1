day=int(input("Enter the number of days:"))
year=day//365
weeks=(day%365)//7
r_days=(day%365)%7
print(year,"year",weeks,"weeks",r_days,"days")