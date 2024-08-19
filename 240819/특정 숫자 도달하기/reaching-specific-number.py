arr=list(map(int,input().split()))
newarr=[]
sumval=0
for elem in arr:
    if elem>=250:
        break
    newarr.append(elem)

for elem in newarr:
    sumval+=elem
print(sumval,f"{sumval/len(newarr):.1f}")