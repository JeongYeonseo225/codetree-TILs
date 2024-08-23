n=int(input())

arr=list(map(int,input().split()))
profit=[]
for i in range(0,4):
    for j in range(i+1,5):
        profit.append(-arr[i]+arr[j])
print(max(profit))