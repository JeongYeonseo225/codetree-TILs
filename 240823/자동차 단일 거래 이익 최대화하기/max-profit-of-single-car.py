n=int(input())

arr=list(map(int,input().split()))
profit=[]
for i in range(0,n-1):
    for j in range(i+1,n):
        profit.append(-arr[i]+arr[j])
print(max(profit))