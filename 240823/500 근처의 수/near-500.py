arr=list(map(int,input().split()))
minarr=[]
maxarr=[]
for elem in arr:
    if elem>500:
        minarr.append(elem)
    elif elem <500:
        maxarr.append(elem)
print(max(maxarr),min(minarr))