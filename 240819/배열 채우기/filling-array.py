arr=list(map(int,input().split()))
newarr=[]

for elem in arr:
    if elem==0:
        break
    newarr.append(elem)

for elem in newarr[::-1]:
    print(elem, end=' ')