n=int(input())
arr=[]
cnt=0
i=1
while True:
    arr.append(n*i)
    i+=1
    if (n*i)%5==0:
        cnt+=1
    if cnt==2:
        arr.append(n*i)
        break

for elem in arr:
    print(elem, end=' ')