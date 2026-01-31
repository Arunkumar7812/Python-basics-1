P=int(input("Enter principal amount: "))
R=int(input("Enter rate of interest: "))
T=int(input("Enter time in years: "))
CI=P*(1+R/100)**T - P
print("Compound Interest is:",CI)