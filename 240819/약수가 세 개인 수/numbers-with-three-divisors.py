arr=input().split()

start=int(arr[0])
end=int(arr[1])

num=0
for i in range(start,end+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==3:
        num+=1
print(num)