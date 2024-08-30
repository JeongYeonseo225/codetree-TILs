a,b=input().split()
aa,bb="",""
for elem in a:
    if elem.isdigit()==True:
        aa+=elem
    else:
        break

for elem in b:
    if elem.isdigit()==True:
        bb+=elem
    else:
        break

print(int(aa)+int(bb))