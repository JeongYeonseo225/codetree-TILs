n=int(input())

for i in range(1,n+1):  #1~3
    for blank in range(n-i):
        print(' ',end='')
    for j in range(i):
        print('*',end=' ')
    print()

for i in range(n+1,2*n):  #4~5
    for blank in range(i-n):
        print(' ',end='')
    for j in range(2*n-i):
        print('*',end=' ')
    print()