arr=list(map(int,input().split()))
newarr=[]

for elem in arr:
    if elem%3==0:
        break
    newarr.append(elem)

print(newarr[-1])