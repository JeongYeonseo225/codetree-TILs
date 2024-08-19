arr=list(map(int,input().split()))
newarr=[]

for elem in arr:
    if elem==0:
        break
    newarr.append(elem)

print(sum(newarr), f"{sum(newarr)/len(newarr):.1f}")