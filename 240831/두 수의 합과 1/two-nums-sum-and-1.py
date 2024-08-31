a,b=tuple(map(int,input().split()))

sumval = a+b
cnt=0
for elem in str(sumval):
    if elem=='1':
        cnt+=1

print(cnt)