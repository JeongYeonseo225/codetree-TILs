msg1=input()
msg2=input()
num1,num2="",""

for elem in msg1:
    if elem.isdigit() ==True:
        num1+=elem

for elem in msg2:
    if elem.isdigit()==True:
        num2+=elem

print(int(num1)+int(num2))