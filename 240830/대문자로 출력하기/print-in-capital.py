msg=input()
alpha=""
for elem in msg:
    if elem.isalpha() ==True:
        alpha+=elem
print(alpha.upper())