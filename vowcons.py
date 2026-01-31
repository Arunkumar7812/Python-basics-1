a=input()
vowel="aeiouAEIOU"
if len(a)==1 and a.isalpha:
    if a in vowel:
        print("vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")