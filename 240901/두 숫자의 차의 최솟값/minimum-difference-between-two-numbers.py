n=int(input())

arr=list(map(int,input().split()))

subarr=[]

for j in range(1,n):
    for i in range(0,n-j):
        sub=abs(arr[i]-arr[i+j])
        subarr.append(sub)

print(min(subarr))