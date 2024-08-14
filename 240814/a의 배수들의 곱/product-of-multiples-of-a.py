arr=input().split()
a=int(arr[0])
b=int(arr[1])

mulval=1
for i in range(1,b+1):
    if i%a==0:
        mulval*=i
print(mulval)