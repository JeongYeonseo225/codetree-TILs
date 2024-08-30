msg=input()
num=[]
for elem in msg:
    if elem.isdigit()==True:
        num.append(int(elem))

print(sum(num))