n=int(input())

sumval=0
for i in range(1,101):
    sumval+=i
    if sumval>=n:
        break
print(i)