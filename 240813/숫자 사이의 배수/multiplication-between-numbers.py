arr=input().split()
a=int(arr[0])
b=int(arr[1])

sumval=0
cnt=0
for i in range(a,b+1):
    if i%5==0 or i%7==0:
        sumval+=i
        cnt+=1
print(f"{sumval} {sumval/cnt:.1f}")