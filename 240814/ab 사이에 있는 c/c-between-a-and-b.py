arr=input().split()
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

sat=False
for i in range(a,b+1):
    if i%c==0:
        sat=True
if sat==True:
    print('YES')
else:
    print('NO')