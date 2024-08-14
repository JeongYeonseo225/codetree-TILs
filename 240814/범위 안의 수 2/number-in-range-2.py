sumval=0
cnt=0
for _ in range(10):
    n=int(input())
    if 0<=n<=200:
        sumval+=n
        cnt+=1
print(sumval,f"{sumval/cnt:.1f}")