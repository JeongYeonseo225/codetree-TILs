n=int(input())
sumval=0

for _ in range(n):
    num=int(input())
    if num%2==1 and num%3==0:
        sumval+=num
print(sumval)