arr=list(map(int,input().split()))
newarr=[]
for n in arr:
    if n==999 or n==-999:
        break
    newarr.append(n)

print(max(newarr),min(newarr))