msg=input()
alphadigit=""
for elem in msg:
    if elem.isalpha()==True or elem.isdigit()==True:
        alphadigit+=elem
print(alphadigit.lower())