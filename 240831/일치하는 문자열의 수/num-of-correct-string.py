arr=input().split()
n=int(arr[0])
A=arr[1]

cnt=0
for _ in range(n):
    msg=input()
    if msg==A:
        cnt+=1
print(cnt)