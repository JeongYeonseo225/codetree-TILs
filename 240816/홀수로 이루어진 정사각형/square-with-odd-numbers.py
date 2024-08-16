n=int(input())

first=11
for i in range(n):
    for j in range(n):
        print(first+2*j,end=' ')
    first+=2
    print()