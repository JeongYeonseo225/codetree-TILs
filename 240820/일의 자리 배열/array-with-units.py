m,n=map(int,input().split())
arr=[]
arr.append(m)
arr.append(n)
for i in range(2,10):
    num=arr[i-2]+arr[i-1]
    num%=10
    arr.append(num)

for elem in arr:
    print(elem,end=' ')