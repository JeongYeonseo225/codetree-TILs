arr=list(map(int,input().split()))
newarr=[]

for elem in arr:
    if elem ==0:
        break
    newarr.append(elem)

for elem in newarr:
    if elem%2==1:
        print(elem+3, end=' ')
    else:
        print(elem//2, end=' ')