n=int(input())

quo=n
cnt=0
for i in range(1,n):
    quo//=i
    cnt+=1
    if quo<=1:
        break
print(cnt)