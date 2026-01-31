a=input()
if a.isalpha() and len(a)==1:
    print("Alphabet")
elif a.isdigit() and len(a)==1:
    print("Digit")
else:
    print("Special chracter")