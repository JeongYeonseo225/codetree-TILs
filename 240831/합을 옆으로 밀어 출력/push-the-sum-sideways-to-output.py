n=int(input())

sumval=0
for _ in range(n):
    num=int(input())
    sumval+=num
sumval=str(sumval)
print(sumval[1:]+sumval[0])