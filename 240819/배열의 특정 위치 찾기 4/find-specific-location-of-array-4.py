arr=list(map(int,input().split()))
newarr=[]

for elem in arr:
    if elem==0:
        break
    newarr.append(elem)

cnt=0
sumval=0
for elem in newarr:
    if elem%2==0:
        cnt+=1
        sumval+=elem

print(cnt,sumval)