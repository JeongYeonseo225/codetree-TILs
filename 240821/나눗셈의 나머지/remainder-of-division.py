arr=input().split()
a=int(arr[0])
b=int(arr[1])

rem=[0] *b
while a>1:
    quo=a//b
    rem[a%b]+=1
    a=quo

sumval=0
for i in range(b):
    sumval+=rem[i]**2
print(sumval)