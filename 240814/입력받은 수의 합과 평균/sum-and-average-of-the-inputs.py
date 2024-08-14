n=int(input())

sumval=0
for _ in range(n):
    intval=int(input())
    sumval+=intval
print(sumval,f"{sumval/n:.1f}")