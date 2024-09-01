n=int(input())

arr=list(map(int,input().split()))
subarr=[]

for j in range(1,n):
    for i in range(n-1,j-1,-1):
        subarr.append(arr[i]-arr[i-j])

if max(subarr)<0:
    print(0)
else:
    print(max(subarr))