arr=input().split()
a=int(arr[0])
b=int(arr[1])

sumval=0
if a>=b:
    for i in range(b,a+1):
        if i%5==0:
            sumval+=i
else:
    for i in range(a,b+1):
        if i%5==0:
            sumval+=i
print(sumval)