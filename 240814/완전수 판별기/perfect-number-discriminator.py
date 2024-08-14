n=int(input())
sumval=0
for i in range(1, n):
    if n%i==0:
        sumval+=i
if sumval==n:
    print('P')
else:
    print('N')