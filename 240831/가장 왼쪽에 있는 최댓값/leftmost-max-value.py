n=int(input())

arr=list(map(int,input().split()))

maxidx = arr.index(max(arr))+1 #4
print(maxidx,end=' ')

while maxidx!=1:
    newarr=[]
    for i in range(maxidx-1):
        newarr.append(arr[i])
    maxidx = newarr.index(max(newarr)) + 1
    print(maxidx,end=' ')