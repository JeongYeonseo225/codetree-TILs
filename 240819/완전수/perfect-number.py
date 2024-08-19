arr=input().split()
start=int(arr[0])
end=int(arr[1])

cnt=0
for i in range(start,end+1):
    sumval=0
    for j in range(1,i):
        if i%j==0:
            sumval+=j
    if sumval==i: #중간에 같아질수동 있어서,,,,
        cnt+=1
print(cnt)