n=int(input())
arr=list(map(int,input().split()))
newarr=[]

for elem in arr:
    if arr.count(elem) >=2:
        continue
    newarr.append(elem)
if len(newarr)==0:
    print(-1)
else:
    print(max(newarr))